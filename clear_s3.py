import sys

import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket(sys.argv[1])
bucket.objects.all().delete()

print("Deleting the all data in ", sys.argv[1])
