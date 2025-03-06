import json
import logging
import boto3
from botocore.exceptions import ClientError


def get_keys(secret_name: str):
    region_name = "eu-central-1"
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        import os
        from dotenv import load_dotenv
        load_dotenv()
        return os.getenv(secret_name)
    return json.loads(get_secret_value_response['SecretString'])[secret_name]


NEWS_URL = get_keys("NEWS_URL")
MISTRAL_API_KEY = get_keys("MISTRAL_API_KEY")
