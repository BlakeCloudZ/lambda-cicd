import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hi! Friendly greeting from the CICD GitHub Actions workflow in VSCode')
    }