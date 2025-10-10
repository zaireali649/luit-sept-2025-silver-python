from helpers import (
    create_ubuntu_instance,
    create_amazon_linux_2023_instance,
    create_amazon_linux_2_instance,
    get_ec2_client,
)


def create_instances(
    ec2_client: object, ami_type: str = "ubuntu", instance_amount: int = 1
) -> None:
    """
    Create one or more EC2 instances based on the specified AMI type.

    Args:
        ec2_client (object): Boto3 EC2 client used to create instances.
        ami_type (str, optional): The type of AMI to use. Supported values:
            - "ubuntu"
            - "linux2023"
            - "linux2"
            Defaults to "ubuntu".
        instance_amount (int, optional): The number of instances to create. Defaults to 1.

    Returns:
        None
    """
    # Normalize the AMI type string (e.g., " Ubuntu " -> "ubuntu", "Linux 2023" -> "linux2023")
    cleaned_ami_type: str = ami_type.lower().strip().replace(" ", "")

    # Create the requested number of instances
    for i in range(instance_amount):
        if cleaned_ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)  # Call helper to create Ubuntu instance
            print("Ubuntu Created")
        elif cleaned_ami_type == "linux2023":
            create_amazon_linux_2023_instance(
                ec2_client
            )  # Call helper to create Amazon Linux 2023 instance
            print("Linux 2023 Created")
        elif cleaned_ami_type == "linux2":
            create_amazon_linux_2_instance(
                ec2_client
            )  # Call helper to create Amazon Linux 2 instance
            print("Linux 2 Created")
        else:
            # Handle unsupported AMI types gracefully
            print("Unsupported AMI")


if __name__ == "__main__":
    # Get the EC2 client
    ec2_client = get_ec2_client()

    # Example usage with different AMI types and amounts
    create_instances(ec2_client)  # Default Ubuntu, 1 instance
    create_instances(ec2_client, ami_type="Linux 2", instance_amount=3)
    create_instances(ec2_client, ami_type="ubuntu")
    create_instances(ec2_client, ami_type="ubuNtu")
    create_instances(ec2_client, ami_type="linUx 2023")
    create_instances(ec2_client, ami_type="linUx 2023 ")
    create_instances(ec2_client, ami_type=" linUx 2023 ")
    create_instances(ec2_client, ami_type="linUx  2023 ")
