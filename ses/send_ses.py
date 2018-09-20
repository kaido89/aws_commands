import boto3
client_sts = boto3.client('sts')
arn = 'arn:aws:iam::Account-ID:role/Send_SES_Role'
response = client_sts.assume_role(RoleArn=arn, RoleSessionName='ses_session')
session_sts = boto3.Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
                            aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                            aws_session_token=response['Credentials']['SessionToken'], region_name='us-east-1')
client_ses = session_sts.client("ses")
response = client_ses.send_email(
    Source='from@email.com',
    Destination={
        'ToAddresses': [
            'from@email.com',
        ],
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'This is the message body in text format.',
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Test email',
        },
    },

)
