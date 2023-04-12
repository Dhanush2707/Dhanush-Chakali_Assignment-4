import boto3

sns_client = boto3.client('sns')

response = sns_client.create_topic(
    Name='my-topic'
)

topic_arn = response['TopicArn']

response = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='dxc74730@ucmo.edu'
)

print(response['SubscriptionArn'])

response = sns_client.publish(
    TopicArn=topic_arn,
    Subject='Test message for SNS',
    Message='Assignment-4')
