import json
import boto3

def get_volume_id_from_arn(volume_arn):
    
    #Split the ARN using the colon seperator
    arn_parts = volume_arn.split(':')
    
    #The volume ID is the last part of the ARN after the 'volume/' prefix
    volume_id = arn_parts[-1].split('/')[-1]
    
    return volume_id

def lambda_handler(event, context):
    
    vol_arn = event['resources'][0]
    vol_id = get_volume_id_from_arn(vol_arn)


    ec2_client = boto3.client('ec2')
    
    response = ec2_client.modify_volume(
        VolumeId=vol_id,
        VolumeType='gp3',
    )
