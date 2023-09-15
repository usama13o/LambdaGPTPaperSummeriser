import json
import os
import urllib.parse
import boto3
import chat_paper as chat
print('Loading function')

s3 = boto3.client('s3')

#test locally
def handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        #create dirs if not exits
        os.makedirs('/tmp/{}'.format(key))
        #download file
        s3.download_file(bucket, key, '/tmp/{}'.format(key))
        chat.chat_paper_main(pdf_path='/tmp/{}'.format(key))
        
        return 'Done!'
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e