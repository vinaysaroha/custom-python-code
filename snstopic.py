import boto3

aws_region = "ap-southeast-2"

sns_client = boto3.client('sns', region_name=aws_region)

def list_topics():

    """

    Lists all SNS notification topics using paginator.

    """

    try:

 

        paginator = sns_client.get_paginator('list_topics')

 

        # creating a PageIterator from the paginator

        page_iterator = paginator.paginate().build_full_result()

 

        topics_list = []

        # loop through each page from page_iterator

        for page in page_iterator['Topics']:

            topics_list.append(page['TopicArn'])

    except Exception as e:

        print(e)

    else:

        return topics_list

 

return_output = list_topics()

for i in return_output:

    try:

        sns_attributes = sns_client.get_topic_attributes(TopicArn=i)

        output=sns_attributes['Attributes']['KmsMasterKeyId']

    except Exception as e:

        print(f"sns topic ARN not having kms is: {i}")

