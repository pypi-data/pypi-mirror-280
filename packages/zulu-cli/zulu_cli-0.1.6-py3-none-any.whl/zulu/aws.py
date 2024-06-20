import boto3
import os
from typing import Any, Dict

def assume_role(role_arn: str, external_id: str, session_name: str = "AssumeRoleSession") -> Dict[str, str]:
    sts_client = boto3.client('sts')

    try:
        assumed_role_object = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name,
            ExternalId=external_id
        )
        credentials = assumed_role_object['Credentials']
        return {
            'AccessKeyId': credentials['AccessKeyId'],
            'SecretAccessKey': credentials['SecretAccessKey'],
            'SessionToken': credentials['SessionToken']
        }
    except Exception as e:
        print(f"Error assuming role {role_arn}: {str(e)}")
        raise e

def get_secret(secret_name: str, region_name: str) -> Dict[str, Any]:
    role_arn = os.getenv('AWS_ASSUME_ROLE_ARN')
    external_id = os.getenv('AWS_ASSUME_ROLE_EXTERNAL_ID')

    if not role_arn or not external_id:
        raise ValueError("Environment variables AWS_ASSUME_ROLE_ARN and AWS_ASSUME_ROLE_EXTERNAL_ID must be set")

    credentials = assume_role(role_arn, external_id)

    client = boto3.client(
        'secretsmanager',
        region_name=region_name,
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken']
    )

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        print(get_secret_value_response )

        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return secret
        else:
            raise ValueError("The secret value is binary and cannot be processed in this script.")

    except Exception as e:
        print(f"Error retrieving secret {secret_name}: {str(e)}")
        raise e
