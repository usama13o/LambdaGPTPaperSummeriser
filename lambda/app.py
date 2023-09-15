import json
import os
import urllib.parse
import boto3
import chat_paper as chat
print('Loading function')

s3 = boto3.client('s3')

#test locally - 
"""
Need to move to a model that sends the pdf name and finds it in the s3 bucket and adds the summary to the
notion page for that pdf
#1 - get the pdf name from the s3 bucket
#2 - run the summary on the pdf
#3 - add the summary to the notion page

"""
def handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the latest object uploaded to the bucket
    bucket = event['Records'][0]['s3']['bucket']['name']
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    latest_obj = None
    for obj in bucket.objects.all():
        if not latest_obj or obj.last_modified > latest_obj.last_modified:
            latest_obj = obj

    # Download the latest object to /tmp
    key = latest_obj.key
    print('Downloading {} from bucket {}...'.format(key, bucket.name))
    try:
        s3 = boto3.client('s3')
        # make sure dirs exist
        if not os.path.exists('/tmp'):
            os.makedirs('/tmp')
            print(os.listdir('./'))
        s3.download_file(bucket.name, key, '/tmp/{}'.format(key.split('/')[-1]))
        chat.chat_paper_main(pdf_path='/tmp/{}'.format(key.split('/')[-1]))
        
        return 'Done!'
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket.name))
        raise e