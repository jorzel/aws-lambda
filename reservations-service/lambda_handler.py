import json
import boto3

client = boto3.client('ses', region_name='eu-central-1')


def lambda_handler(event, context):
    data = json.loads(event['Records'][0]['Sns']['Message'])
    body = data.get('body')
    email = data.get('email')

    response = client.send_email(
        Destination={
            'ToAddresses': ['verified@mail.com']
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': body,
                }
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Reservation email to:' + email,
            },
        },
        Source='verified@mail.com'
    )
    print("Send mail to:" + email)
    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully. MessageId is: " + response['MessageId'])
    }
