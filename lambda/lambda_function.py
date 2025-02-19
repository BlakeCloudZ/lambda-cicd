import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello! A friendly greeting from the CICD GitHub Actions workflow in VSCode')
    }