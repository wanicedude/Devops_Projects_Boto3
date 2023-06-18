import boto3



def Get_Image(client):
    Image = client.describe_images(
       Filters=[
        {
            'Name': 'name',
            'Values': [
                'amzn2-ami-hvm*',
            ],
        },
        {
            
            'Name': 'owner-alias',
            'Values': [
                'amazon',
            ],
        },
    ],
    )
    AMI = Image['Images'][0]['ImageId']
    return(AMI)

def Create_instance(resources,AMI):
    instance = resources.create_instances(
        ImageId = AMI,
        MinCount = 1,
        MaxCount = 1,
        InstanceType = "t2.micro",
    )
    return instance

def List_intances(resource):
    for instance in resource.instances.all():
        print(instance.id,instance.state['Name'])
        
def Stop_instance(resource):
    for instance in resource.instances.all():
       instance.stop()
        
    
    
if __name__ == "__main__":    
    
    # Ec2 Client & Resource
    Ec2_client = boto3.client("ec2")
    Ec2_reso = boto3.resource("ec2")

    #Get Image from the Get Image function
    AMI = Get_Image(Ec2_client)

    #Create Instance using the Image and resource
    instance  = Create_instance(Ec2_reso,AMI)

    #list instance
    List_intances(Ec2_reso)
   
   #Stop instance
    Stop_instance(Ec2_reso)