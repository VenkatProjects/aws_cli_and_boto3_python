import boto3
import sys

# Create an EC2 resource
ec2_resource = boto3.resource('ec2')

# Retrieve the instance ID from command-line argument
if len(sys.argv) < 2:
    print("Please provide the instance ID as a command-line argument.")
    sys.exit(1)
instance_id = sys.argv[1]
# Retrieve the instance object
instance = ec2_resource.Instance(instance_id)
# Terminate the instance
try:
    instance.terminate()
    print(f"Terminating EC2 Instance {instance_id}...")
    print("Termination successful!")
except Exception as e:
    print("Error occurred while terminating the instance:", str(e))

