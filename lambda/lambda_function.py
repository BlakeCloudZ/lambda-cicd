import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hey! Friendly greeting from the CICD GitHub Actions workflow in VSCode')
    }