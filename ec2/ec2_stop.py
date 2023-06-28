import boto3

# Create an EC2 resource
ec2_resource = boto3.resource('ec2')

# Retrieve the instance object
instance = ec2_resource.Instance('i-03233c80d285b1a17')

# Start the instance
instance.start()

# Stop the instance
#instance.stop()

