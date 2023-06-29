import boto3

# Create an EC2 resource
ec2_resource = boto3.resource('ec2')

# Create an instance
instance = ec2_resource.create_instances(
        ImageId='ami-0d2f97c8735a48a15',
        InstanceType='t2.micro',
        MinCount=1, #Enter number instance you want
        MaxCount=1, 
        KeyName='test2devops',
        SecurityGroupIds=['sg-079b0d65af0d1fd'],
        SubnetId='subnet-0ed9764e7d7254629b7b'
     )
# Access the created instance's ID
instance_id = instance[0].instance_id
print(f"Created EC2 Instance ID: {instance_id}")
