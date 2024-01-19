import boto3
import sys

client = boto3.client('cloudformation')

response = client.delete_stack(
    StackName=sys.argv[1]
)

print("Deleting the Stack: ", response)
