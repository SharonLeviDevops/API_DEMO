# "SumFunction" the aws lambda function
import boto3
import json


def lambda_handler(event, context):
    # TODO implement
    print(event)
    GET_RAW_PATH = "/get"
    client = boto3.client('sns')
    snsArn = 'arn:aws:sns:us-east-1:700935310038:MailToClient'
    message = "This is a test notification."
    number1 = event.get("num1")
    number2 = event.get("num2")
    value = {
        "num1": number1,
        "num2": number2,
    }

    response = client.publish(
        TopicArn=snsArn,
        Message=message,
        Subject=f"Sum of number is: {number1 + number2}"
    )
        
    return {
        'statusCode': 200,
        'body': json.dumps(f"Sum Of numbers :{value}")
    }
        
