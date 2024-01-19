# CD12352 - Infrastructure as Code Project Solution

# Heshan Muhandiramlage

## Prerequisites

- Install Python 3
- Install AWS CLI V2

## Spin up instructions

#### In order to create the stack please use the following command

python3 create.py stack-name template.yml parameters.json

### Steps

##### 1- Create Networking Stack

python3 create.py udacity-project-2-networking-resources network.yml network-parameters.json

##### 2- Create Application Infrastructure

python3 create.py udacity-project-2-application-resources udagram.yml udagram-parameters.json

## Update Instructions

#### In order to create the stack please use the following command

python3 update.py stack-name template.yml parameters.json

### Steps

##### 1- Update Networking Stack

python3 update.py udacity-project-2-networking-resources network.yml network-parameters.json

##### 2- Update Application Infrastructure

python3 update.py udacity-project-2-application-resources udagram.yml udagram-parameters.json

## SSH to EC2 Instances through Bastion Host
ssh -J bastion_user@bastion_server_dns ec2_user@ec2_ip

Example:
ssh -J ubuntu@ec2-54-82-53-54.compute-1.amazonaws.com ubuntu@10.0.6.165

## Tear down instructions

#### In order to clear S3 Bucket please use the following command

python3 clear_s3.py bucket_name

#### In order to delete the stack please use the following command

python3 delete.py stack-name

### Steps

#### 1 - Make sure s3 bucket is empty

pytho3 clear_s3.py us-east-1-udacity-project-2-bucket

##### 2- Update Application Infrastructure

python3 delete.py udacity-project-2-application-resources

##### 3- Update Networking Infrastructure

python3 delete.py udacity-project-2-networking-resources
