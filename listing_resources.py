from helpers import list_buckets, describe_instances, get_ec2_client, get_s3_client


def print_bucket_names(s3_client: object) -> None:
    """
    Prints the names of all S3 buckets available for the given client.

    Args:
        s3_client (object): An authenticated boto3 S3 client used to list buckets.

    Returns:
        None
    """
    # Retrieve list of bucket names using a helper function
    bucket_names = list_buckets(s3_client)

    # Iterate through and print each bucket name
    for bucket_name in bucket_names:
        print(bucket_name)


def print_instance_ids(ec2_client: object) -> None:
    """
    Prints the instance IDs of all EC2 instances for the given client.

    Args:
        ec2_client (object): An authenticated boto3 EC2 client used to describe instances.

    Returns:
        None
    """
    # Retrieve a list of EC2 instances using a helper function
    instances = describe_instances(ec2_client)

    # Extract instance IDs into a list
    instance_ids: list[str] = []
    for instance in instances:
        instance_ids.append(instance["InstanceId"])

    # Print each EC2 instance ID
    for instance_id in instance_ids:
        print(instance_id)


if __name__ == "__main__":
    # Initialize AWS clients for EC2 and S3 using helper functions
    ec2_client = get_ec2_client()
    s3_client = get_s3_client()

    # Print all S3 bucket names
    print_bucket_names(s3_client)

    # Print all EC2 instance IDs
    print_instance_ids(ec2_client)
