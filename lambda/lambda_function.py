import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Howdy!! Sending love from the CICD GitHub Actions workflow in VSCode')
    }