from ast import Try
import json
import pyqrcode
import png
from pyqrcode import QRCode
import boto3

def lambda_handler(event, context):
    s = "www.apple.com"
    file_name = 'myqr.png'
    url = pyqrcode.create(s)
    url.png('/tmp/' + file_name, scale = 6)

    s3 = boto3.client('s3')
    bucket = 'boxie-qrcodes'

    try:
        s3.upload_file('/tmp/' + file_name, bucket, file_name)
    except:
        return {
            'statusCode': 500,
            'body': json.dumps('S3 save not successful')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('Generated QR code success')
        }
