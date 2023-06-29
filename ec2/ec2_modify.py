import boto3
import sys

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Retrieve the instance ID and instance type from command-line arguments
if len(sys.argv) < 3:
    print("Please provide the instance ID and instance type as command-line arguments.")
    sys.exit(1)
instance_id = sys.argv[1]
instance_type = sys.argv[2]
# Modify instance attributes
try:
    response = ec2_client.modify_instance_attribute(
            InstanceId=instance_id,
            Attribute='instanceType',
            Value=instance_type
            )
    print(f"Modifying EC2 Instance {instance_id} with instance type {instance_type}...")
    print("Modification successful!")
except Exception as e:
    print("Error occurred while modifying the instance:", str(e))

