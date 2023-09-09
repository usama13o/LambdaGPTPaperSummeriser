import json
import boto3
from moto import mock_s3
from app import lambda_handler


@mock_s3
def test_lambda_handler():
    # Create a mock S3 bucket and object
    s3 = boto3.resource('s3', region_name='us-east-1')
    bucket_name = 'test-bucket'
    s3.create_bucket(Bucket=bucket_name)
    object_key = 'test-object'
    s3.Object(bucket_name, object_key).put(Body=b'test content')

    # Call the lambda_handler function with a mock S3 event
    event = {
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "eu-west-1",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "responseElements": {
        "x-amz-request-id": "EXAMPLE123456789",
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "testConfigRule",
        "bucket": {
          "name": "paper-summarizer",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::paper-summarizer"
        },
        "object": {
          "key": "Restoring Vision in Adverse Weather Conditions with Patch-Based Denoising Diffusion Models.pdf",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901"
        }
      }
    }
  ]
}
    result = lambda_handler(event, None)

    # Assert that the function returns the expected file content
    assert result == b'test content'