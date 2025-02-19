import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello! Sending love from our CICD GitHub Actions workflow in VSCode')
    }