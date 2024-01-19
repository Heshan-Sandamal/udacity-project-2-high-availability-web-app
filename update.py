import boto3, sys, json

client = boto3.client('cloudformation')

with open(sys.argv[2], 'r') as content_file:
    cft_template = content_file.read()

params = json.load(open(sys.argv[3]))

response = client.update_stack(
    StackName=sys.argv[1],
    TemplateBody=cft_template,
    Parameters=params,
    Capabilities=[
        'CAPABILITY_IAM',
        'CAPABILITY_NAMED_IAM'
    ],
)

print("Updating the Stack ARN: ", response["StackId"])
