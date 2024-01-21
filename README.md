# CD12352 - Infrastructure as Code Project Solution

# Heshan Muhandiramlage

## Prerequisites

- Install Python 3
- Install AWS CLI V2

## Spin up instructions

#### In order to create the stack please use the following command

python3 scripts/create.py stack-name template.yml parameters.json

### Steps

##### 1- Create Networking Stack

python3 scripts/create.py udacity-project-2-networking-resources network.yml network-parameters.json

##### 2- Create Application Infrastructure

python3 scripts/create.py udacity-project-2-application-resources udagram.yml udagram-parameters.json

## Update Instructions

#### In order to update the stack please use the following command

python3 scripts/update.py stack-name template.yml parameters.json

### Steps

##### 1- Update Networking Stack

python3 scripts/update.py udacity-project-2-networking-resources network.yml network-parameters.json

##### 2- Update Application Infrastructure

python3 scripts/update.py udacity-project-2-application-resources udagram.yml udagram-parameters.json

## SSH to EC2 Instances through Bastion Host

##### 1- Get Private Key & Create .pem file with the key

python3 scripts/get_secret.py bastion-host-private-key

#### 2 - Configure proper permissions and ssh agent

Example: (using gitbash in windows)

- eval $(ssh-agent -s)
- ssh-add my-udacity-keypair.pem

##### 3 - SSH to instance

ssh -J bastion_user@bastion_server_dns ec2_user@ec2_ip

Example:
ssh -J ubuntu@ec2-54-82-53-54.compute-1.amazonaws.com ubuntu@10.0.6.165

## Tear down instructions

#### In order to clear S3 Bucket please use the following command

python3 scripts/clear_s3.py bucket_name

#### In order to delete the stack please use the following command

python3 scripts/delete.py stack-name

### Steps

#### 1 - Make sure s3 bucket is empty

python3 scripts/clear_s3.py us-east-1-udacity-project-2-bucket

##### 2- Delete Application Infrastructure & wait until it completes

python3 scripts/delete.py udacity-project-2-application-resources

##### 3- Delete Networking Infrastructure

python3 scripts/delete.py udacity-project-2-networking-resources

### Other Details

#### 1. If cloudfront shows access denied page

Upload a file to s3 bucket through console or doing ssh to instance and then upload from instance
Then that file should be able to be accessed through cloudfront or directly using the s3 url

Eg: if index.html is uploaded to the bucket, It can be accessed using following urls

https://us-east-1-udacity-project-2-bucket.s3.amazonaws.com/index.html
https://{cloud-front-assigned-name}.cloudfront.net/index.html

