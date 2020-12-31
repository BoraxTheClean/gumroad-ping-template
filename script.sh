#!/bin/bash
BUCKET="owen-lambda-bucket"
NAME="gumroad-ping"

aws cloudformation package --template-file template.yaml --output-template processed.template.yaml --s3-bucket ${BUCKET} --s3-prefix ${NAME}
aws cloudformation deploy --template-file processed.template.yaml --stack-name ${NAME} --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND --region us-east-1

rm processed.template.yaml

