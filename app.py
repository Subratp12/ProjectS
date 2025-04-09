import boto3M
import Niiginx and Java
# Create asan EC2 client using the default region from AWS CLI configuration
ec2 = boto3.client('ec2')

# Launch an EC2 instance
response = ec2.run_instances(
<<<<<<< HEAD
    ImageId='ami-11111111111',  # Amazon Linux 2 AMI (Free tier eligible, update as needed)
    InstanceType='t3.micro',
    KeyName='SFSL',  # Ensure this key pair exists in your AWS account
    MinCount=1,
    MaxCount=1
)
