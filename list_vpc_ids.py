import boto3  # AWS SDK for Python, provides an interface to AWS services

# Create an EC2 client to interact with VPC-related operations
vpc_client = boto3.client("ec2")

# Call the describe_vpcs method to get information about all VPCs in the account
response = vpc_client.describe_vpcs()

# Extract the list of VPCs from the response dictionary
vpcs = response["Vpcs"]

# Loop through each VPC in the list and print its unique VPC ID
for vpc in vpcs:
    print(vpc["VpcId"])
