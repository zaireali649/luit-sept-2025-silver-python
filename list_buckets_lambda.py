import json
import boto3  # AWS SDK for Python, used to interact with AWS services like S3

def lambda_handler(event, context):
    # Create an S3 client to communicate with the S3 service
    s3 = boto3.client("s3")

    # Call the list_buckets method to retrieve all buckets in the account
    response = s3.list_buckets()

    # Extract the list of buckets from the response dictionary
    buckets = response["Buckets"]

    bucket_names = []

    # Loop through each bucket in the list and print its name
    for bucket in buckets:
        print(bucket["Name"])
        bucket_names.append(bucket["Name"])

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(bucket_names)
    }
