import json
import boto3

client = boto3.client('connect')

def lambda_handler(event, context):
    print(event)
    if event['Records'][0]['eventName'] == "INSERT" :
        for record in event['Records']:
            phone_number = record['dynamodb']['Keys']['phone']['S']
            data = record['dynamodb']['NewImage']
            print(phone_number)
            data = json.dumps(data)

        response = client.start_outbound_voice_contact(
            Name='DDB call',
            Description=data,
            DestinationPhoneNumber=phone_number,
            ContactFlowId='xxxxx',
            InstanceId='xxxx',
            QueueId='xxxxx'
            )    
