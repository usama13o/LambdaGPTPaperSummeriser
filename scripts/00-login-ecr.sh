#!/bin/bash
$AWS_REGION = eu-west-1
$AWS_ACCOUNT_ID =   469580660316

aws ecr get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com