from chalice import Chalice, Response
import json, boto3, os
from botocore.exceptions import ClientError

from chalice import NotFoundError

app = Chalice(app_name='helloworld')

s3 = boto3.client('s3', region_name='us-west-2')
BUCKET='chalicetest1'

@app.route('/')
def index():
    try:
        return {'status_code': 200,
                'message': 'welcome to this test API'}
    except:
        return Response(message='Oops! Something went wrong!',
                        headers={'Content-Type': 'text/plain'},
                        stats_code=400)

@app.route('/upload/{file_name}', methods=['PUT'],
           content_types=['application/octet-stream'])
def upload_to_s3(file_name):
    try:
        body = app.current_request.raw_body
        temp_file = '/tmp/' + file_name  # create temp file path
        with open(temp_file, 'wb') as f:
            f.write(body)
        s3.upload_file(temp_file, BUCKET, file_name)
        return Response(message='Successfully uploaded %s'% file_name,
                        headers={'Content-Type': 'text/plain'},
                        status_code=200)
    except Exception, e:
        app.log.error('error occured while uploading %s'% e)
        return Response(message='Upload Failed',
                    headers={'Content-Type': 'text/plain'},
                    stats_code=400)
