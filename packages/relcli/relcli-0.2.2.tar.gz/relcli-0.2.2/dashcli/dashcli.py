import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

import boto3
import click
import pyperclip
from botocore.exceptions import ProfileNotFound, NoCredentialsError, PartialCredentialsError, ClientError
from rich.console import Console
from rich.table import Table

# Constants
DYNAMODB_TABLE = "ecsclusters"
CACHE_DIR = os.path.expanduser("~")
SSL_ROOT_CERTIFICATE = os.path.join(CACHE_DIR, 'us-east-1-bundle.pem')

# Initialize Rich console for pretty printing
console = Console()


def get_cache_file(aws_profile):
    """
    Get the cache file path for the given AWS profile.

    :param aws_profile: The AWS profile name.
    :return: The path to the cache file.
    """
    return os.path.join(CACHE_DIR, f".dashcli_cache_{aws_profile}.json")


def load_cache(cache_file):
    """
    Load cache from the cache file.

    :param cache_file: The path to the cache file.
    :return: The cached data as a dictionary.
    """
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            return json.load(f)
    return {}


def save_cache(cache_file, data):
    """
    Save data to the cache file.

    :param cache_file: The path to the cache file.
    :param data: The data to save.
    """
    with open(cache_file, 'w') as f:
        json.dump(data, f)


def initialize_aws_session(aws_profile, region):
    """
    Initialize AWS session with error handling.

    :param aws_profile: The AWS profile name.
    :param region: The AWS region.
    :return: A boto3 Session object or None if initialization failed.
    """
    try:
        session = boto3.Session(profile_name=aws_profile, region_name=region)
        return session
    except ProfileNotFound:
        click.echo(
            f"The config profile ({aws_profile}) could not be found. Please create one using the following command:")
        click.echo(f"aws configure --profile {aws_profile}")
    except (NoCredentialsError, PartialCredentialsError):
        click.echo("AWS credentials not found or incomplete. Please configure your AWS credentials.")
        click.echo("Use the command: aws configure")
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}")
    return None


def get_user_id(session, refresh, aws_profile):
    """
    Retrieve the username from STS get-caller-identity or cache it as db_user_name.

    :param session: The boto3 Session object.
    :param refresh: A flag indicating whether to refresh the cached data.
    :param aws_profile: The AWS profile name.
    :return: The user ID as db_user_name.
    """
    cache_file = get_cache_file(aws_profile)
    cache = load_cache(cache_file)

    if refresh or 'db_user_name' not in cache:
        sts_client = session.client('sts')
        user_id = sts_client.get_caller_identity()['UserId']
        cache['db_user_name'] = user_id
        save_cache(cache_file, cache)
    else:
        user_id = cache['db_user_name']

    return user_id


def get_clusters(session, aws_profile, region, refresh):
    """
    Retrieve ECS clusters and cache the results.

    :param session: The boto3 Session object.
    :param aws_profile: The AWS profile name.
    :param region: The AWS region.
    :param refresh: A flag indicating whether to refresh the cached data.
    :return: A list of cluster names.
    """
    cache_file = get_cache_file(aws_profile)
    cache = load_cache(cache_file)

    if refresh or 'clusters' not in cache:
        ecs_client = session.client('ecs')
        paginator = ecs_client.get_paginator('list_clusters')
        cluster_arns = []
        for page in paginator.paginate():
            cluster_arns.extend(page['clusterArns'])

        clusters = [arn.split('/')[-1] for arn in cluster_arns]
        cache['clusters'] = clusters
        save_cache(cache_file, cache)
    else:
        clusters = cache['clusters']

    return clusters


def get_services_for_cluster(session, aws_profile, cluster_name, refresh):
    """
    Retrieve services for a given ECS cluster and cache the results.

    :param session: The boto3 Session object.
    :param aws_profile: The AWS profile name.
    :param cluster_name: The name of the ECS cluster.
    :param refresh: A flag indicating whether to refresh the cached data.
    :return: A dictionary of services with their tags.
    """
    cache_file = get_cache_file(aws_profile)
    cache = load_cache(cache_file)

    if refresh or cluster_name not in cache:
        ecs_client = session.client('ecs')
        paginator = ecs_client.get_paginator('list_services')
        service_arns = []
        for page in paginator.paginate(
                cluster=f"arn:aws:ecs:{session.region_name}:{session.client('sts').get_caller_identity()['Account']}:cluster/{cluster_name}"):
            service_arns.extend(page['serviceArns'])

        services = fetch_services_tags_concurrently(ecs_client, service_arns)

        cache[cluster_name] = services
        save_cache(cache_file, cache)
    else:
        services = cache[cluster_name]

    return services


def fetch_services_tags_concurrently(ecs_client, service_arns):
    """
    Fetch tags for multiple ECS services concurrently.

    :param ecs_client: The ECS client.
    :param service_arns: A list of service ARNs.
    :return: A dictionary of services with their tags.
    """
    services = {}
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(get_service_tags, ecs_client, arn): arn for arn in service_arns}
        for future in as_completed(futures):
            service_arn = futures[future]
            service_name = service_arn.split('/')[-1]
            try:
                service_tags = future.result()
                services[service_name] = service_tags
            except Exception as e:
                click.echo(f"Error retrieving tags for {service_arn}: {e}")

    return services


def get_service_tags(ecs_client, service_arn):
    """
    Retrieve tags for a given ECS service.

    :param ecs_client: The ECS client.
    :param service_arn: The ARN of the ECS service.
    :return: A dictionary of service tags.
    """
    try:
        response = ecs_client.list_tags_for_resource(resourceArn=service_arn)
        tags = {tag['key']: tag['value'] for tag in response.get('tags', [])}
        return tags
    except ClientError as e:
        click.echo(f"Failed to retrieve tags for {service_arn}: {e}")
        return {}


def select_cluster(clusters):
    """
    Allow the user to select a cluster.

    :param clusters: A list of cluster names.
    :return: The selected cluster name or None if invalid input.
    """
    for idx, cluster in enumerate(clusters, start=1):
        click.echo(f"{idx}. {cluster}")

    try:
        cluster_index = int(click.prompt("Select a cluster", type=int))
        if 1 <= cluster_index <= len(clusters):
            return clusters[cluster_index - 1]
        else:
            click.echo("Invalid cluster number.")
            return None
    except ValueError:
        click.echo("Invalid input.")
        return None


def select_service(services):
    """
    Allow the user to select a service from the selected cluster.

    :param services: A dictionary of services and their tags.
    :return: The selected service name and its tags, or (None, None) if invalid input.
    """
    service_names = sorted(list(services.keys()))
    for idx, service in enumerate(service_names, start=1):
        service_names.sort()
        click.echo(f"{idx}. {service}")

    try:
        service_index = int(click.prompt("Select a service", type=int))
        if 1 <= service_index <= len(service_names):
            return service_names[service_index - 1], services[service_names[service_index - 1]]
        else:
            click.echo("Invalid service number.")
            return None, None
    except ValueError:
        click.echo("Invalid input.")
        return None, None


def display_tags(service_name, tags, aws_profile):
    """
    Display tags in a formatted table.

    :param service_name: The name of the service.
    :param tags: A dictionary of service tags.
    :param aws_profile: The AWS profile name.
    """
    table = Table(title=f"Service Tags for {service_name}")
    table.add_column("Key", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    sorted_tags = sorted(tags.items(), key=lambda item: (item[0] != "Name", item[0]))
    for key, value in sorted_tags:
        if key == "LOGS":
            value = f"{value} --profile {aws_profile}"
        table.add_row(key, value)

    console.print(table)


def generate_iam_token(session, db_host, db_port, db_user_name):
    """
    Generate an IAM token for connecting to an RDS database.

    :param session: The boto3 Session object.
    :param db_host: The database host.
    :param db_port: The database port.
    :param db_user_name: The database username.
    :return: The IAM token.
    """
    rds_client = session.client('rds')
    token = rds_client.generate_db_auth_token(DBHostname=db_host, Port=int(db_port), DBUsername=db_user_name)
    return token


def connect_to_psql(db_host, db_port, db_name, db_user_name, sslrootcertificate, pg_password):
    """
    Connect to PostgreSQL database using psql command.

    :param db_host: The database host.
    :param db_port: The database port.
    :param db_name: The database name.
    :param db_user_name: The database username.
    :param sslrootcertificate: The path to the SSL root certificate.
    :param pg_password: The password for the database user.
    """
    os.environ['PGPASSWORD'] = pg_password
    psql_command = f'psql "host={db_host} port={db_port} dbname={db_name} user={db_user_name} sslmode=verify-full sslrootcert={sslrootcertificate}"'
    subprocess.run(psql_command, shell=True)


@click.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.argument('aws_profile', required=False, default='dev')
@click.option('--region', default='us-east-1', help='AWS region to use.')
@click.option('--refresh', is_flag=True, help='Refresh cached data.')
@click.option('--psql', is_flag=True, help='Connect to PostgreSQL database using psql.')
def dashcli(aws_profile, region, refresh, psql):
    """
    Main CLI function for managing AWS services and connecting to PostgreSQL databases.

    :param aws_profile: The AWS profile name.
    :param region: The AWS region.
    :param refresh: A flag indicating whether to refresh cached data.
    :param psql: A flag indicating whether to connect to PostgreSQL database using psql.
    """
    session = initialize_aws_session(aws_profile, region)
    if not session:
        return

    db_user_name = get_user_id(session, refresh, aws_profile)

    if not os.path.isfile(SSL_ROOT_CERTIFICATE):
        click.echo(f"SSL root certificate not found at {SSL_ROOT_CERTIFICATE}. Please download it.")
        return

    clusters = get_clusters(session, aws_profile, region, refresh)
    if clusters:
        selected_cluster = select_cluster(clusters)
        if selected_cluster:
            services = get_services_for_cluster(session, aws_profile, selected_cluster, refresh)
            selected_service, tags = select_service(services)
            if selected_service:
                if 'DB_HOST' in tags and 'DB_NAME' in tags and 'DB_PORT' in tags:
                    tags['DB_USER'] = db_user_name
                    display_tags(selected_service, tags, aws_profile)
                    pg_password = generate_iam_token(session, tags['DB_HOST'], tags['DB_PORT'], db_user_name)
                    console.print(f"Generated IAM Token: {pg_password}", style="red")
                    pyperclip.copy(pg_password)
                    click.echo("IAM Token has been copied to the clipboard.")
                    if psql:
                        connect_to_psql(tags['DB_HOST'], tags['DB_PORT'], tags['DB_NAME'],
                                        db_user_name, SSL_ROOT_CERTIFICATE, pg_password)
                else:
                    display_tags(selected_service, tags, aws_profile)


if __name__ == '__main__':
    dashcli()
