from io import BytesIO

import boto3
import requests

from python_dxh.config import settings


def textract_handler(path):
    """Process an image using AWS Textract

    :param image_url: URL of the image to process
    :return: Extracted text data from the image, or None if an error occurs
    """
    textract_client = boto3.client(
        'textract',
        region_name=settings.DJANGO_AWS_TEXTRACT_REGION_NAME,
        aws_access_key_id=settings.DJANGO_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.DJANGO_AWS_SECRET_ACCESS_KEY,
    )
    try:
        response = requests.get(path)
        if response.status_code == 200:
            image_bytes = BytesIO(response.content)
            img = bytearray(image_bytes.getvalue())
            data = textract_client.detect_document_text(
                Document={'Bytes': img}
            )
            return data
        else:
            return response.status_code
    except Exception as e:
        return None
