@REM #!/bin/bash

@REM # docker build -t "$SERVICE_NAME" .
@REM # docker tag "$SERVICE_NAME":latest "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/"$SERVICE_NAME":latest
@REM # docker push "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/"$SERVICE_NAME":latest

@REM # aws lambda update-function-code \
@REM #     --function-name "$SERVICE_NAME" \
@REM #     --image-uri "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/"$SERVICE_NAME":latest
docker build --pull --rm -f "Dockerfile" -t awstest:latest "." 
docker tag awstest 469580660316.dkr.ecr.eu-west-1.amazonaws.com/notion_lambdapdf
docker push 469580660316.dkr.ecr.eu-west-1.amazonaws.com/notion_lambdapdf
aws lambda update-function-code --function-name "lambdaPDFSummary" --image-uri "469580660316.dkr.ecr.eu-west-1.amazonaws.com/notion_lambdapdf:latest"