import logging
import os
from io import BytesIO

import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

from python_dxh.config import settings
import requests


class S3Client:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            region_name=settings.DJANGO_AWS_S3_REGION_NAME,
            aws_access_key_id=settings.DJANGO_AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.DJANGO_AWS_SECRET_ACCESS_KEY,
            config=Config(signature_version='s3v4')
        )
        self.bucket_name = settings.DJANGO_AWS_STORAGE_BUCKET_NAME
    
    def upload_to_s3(self, file_name, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        if object_name is None:
            object_name = os.path.basename(file_name)

        try:
            self.s3_client.upload_fileobj(file_name, self.bucket_name, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def delete_from_s3(self, object_key=None, object_id=None):
        """Delete an object from an S3 bucket

        :param object_key: S3 object key to delete
        :param object_id: Prefix for objects to delete (optional)
        :return: True if object(s) was deleted, else False
        """
        try:
            if object_id is not None:
                objects = self.s3_client.list_objects(Bucket=self.bucket_name, Prefix=object_id)
                key_pattern = f'{object_id}/'
                for obj in objects.get('Contents', []):
                    if object_key and object_key == obj['Key']:
                        self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_key)
                    elif obj['Key'].startswith(key_pattern):
                        self.s3_client.delete_object(Bucket=self.bucket_name, Key=obj['Key'])
            else:
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_key)
        except ClientError as e:
            logging.error(e)
            return False
        except Exception as e:
            logging.error(e)
            return False
        return True
    

