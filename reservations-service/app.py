import boto3
import json
import os
import random

# Initialize SNS client
sns = boto3.client(
    'sns',
    region_name=os.environ.get('REGION'),
    aws_access_key_id=os.environ.get('ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('SECRET_ACCESS_KEY'),
)

# Your SNS Topic ARN
sns_topic_arn = os.environ.get('TOPIC_ARN')


def publish_message(message):
    response = sns.publish(
        TopicArn=sns_topic_arn,
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json',
    )
    print(f"Message published to SNS: {response['MessageId']}")


if __name__ == "__main__":
    r = random.randint(0, 1000000)
    message = {
        'event': 'UserSignup',
        'user_id': '12345',
        'email': f'user+{r}@example.com',
        'body': 'Welcome to our platform!'
    }
    publish_message(message)
