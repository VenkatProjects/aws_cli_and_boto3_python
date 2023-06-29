import boto3
import sys

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Retrieve the instance ID from command-line argument
if len(sys.argv) < 2:
    print("Please provide the instance ID as a command-line argument.")
    sys.exit(1)
instance_id = sys.argv[1]

            # Describe instance status
response = ec2_client.describe_instance_status(
        InstanceIds=[instance_id]
        )

            # Access instance status details
for instance_status in response['InstanceStatuses']:
    instance_id = instance_status['InstanceId']
    status = instance_status['InstanceState']['Name']
                            
                                # Get instance details
instance_response = ec2_client.describe_instances(
        InstanceIds=[instance_id]
        )
reservations = instance_response['Reservations']
if reservations:
    instance = reservations[0]['Instances'][0]
    instance_name = [tag['Value'] for tag in instance['Tags'] if tag['Key'] == 'Name']
    instance_type = instance['InstanceType']
    platform = instance.get('Platform', 'Linux')
    print(f"Instance ID: {instance_id}")
    print(f"Status: {status}")
    print(f"Server Name: {instance_name[0] if instance_name else 'N/A'}")
    print(f"Instance Type: {instance_type}")
    print(f"Platform: {platform}")
    print()

