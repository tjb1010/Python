import boto3
import logging

client = boto3.client('ec2')

instances = []
for region in client.describe_regions()['Regions']:
    ec2 = boto3.resource('ec2', region_name=region['RegionName'])
    result = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in result:
    instances.append(instance.id)
return instances

print instances