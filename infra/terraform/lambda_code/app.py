import boto3
import json
import os


def fetch_secrets():
    secret_name = os.environ.get("LAMBDA_NAME")
    region_name = os.environ.get("AWS_REGION")
    client = boto3.client("secretsmanager", region_name=region_name)

    try:
        response = client.get_secret_value(SecretId=secret_name)
        return json.loads(response["SecretString"])
    except Exception as e:
        raise Exception(f"Error fetching secrets: {e}")


def lambda_handler(event, context):
    try:
        secrets = fetch_secrets()
        return {
            "statusCode": 200,
            "body": json.dumps(
                {"message": "Secrets retrieved successfully!", "secrets": secrets}
            ),
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
