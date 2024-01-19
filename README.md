# CD12352 - Infrastructure as Code Project Solution

# Heshan Muhandiramlage

## Spin up instructions

#### In order to create the stack please use the following command
./create.sh stack-name template.yml parameters.json

### Steps

##### 1- Create Networking Stack
./create.sh udacity-project-2-networking-resources network.yml network-parameters.json

##### 2- Create Application Infrastructure
./create.sh udacity-project-2-application-resources udagram.yml udagram-parameters.json

## Update Instructions

#### In order to create the stack please use the following command
./update.sh stack-name template.yml parameters.json

### Steps

##### 1- Update Networking Stack
./update.sh udacity-project-2-networking-resources network.yml network-parameters.json

##### 2- Update Application Infrastructure
./update.sh udacity-project-2-application-resources udagram.yml udagram-parameters.json

## Tear down instructions

#### In order to create the stack please use the following command
./delete.sh stack-name

### Steps

#### 1 - Make sure s3 bucket is empty

##### 2- Update Application Infrastructure
./delete.sh udacity-project-2-application-resources

##### 3- Update Networking Infrastructure
./delete.sh udacity-project-2-networking-resources
