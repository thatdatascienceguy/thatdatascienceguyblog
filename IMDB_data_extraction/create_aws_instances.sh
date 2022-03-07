#!/bin/bash

aws ec2 create-key-pair --key-name "testing-key"
aws ec2 run-instances --image-id ami-033b95fb8079dc481 --key-name "testing-key" \
	--security-groups default \
	--instance-type c5.2xlarge \
	--placement AvailabilityZone=us-east-1a \
	--count 2 \
	--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=imdb-server}]'
