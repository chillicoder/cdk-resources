from aws_cdk import core as cdk
from aws_cdk import aws_ec2 as ec2

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CdkResourcesStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, cidr: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc(
            self, "ThisVpc",
            cidr=cidr,
            max_azs=3,
            subnet_configuration=[{
                'subnetType': ec2.SubnetType.PUBLIC,
                'name': 'Public',
                'cidr_mask': 25
            },{
                'subnetType': ec2.SubnetType.PRIVATE,
                'name': 'Private',
                'cidr_mask': 24
            },{
                'subnetType': ec2.SubnetType.ISOLATED,
                'name': 'Isolated',
                'cidr_mask': 26
            }]
        )

        bastion = ec2.BastionHostLinux(
            self, "ThisBastionHost",
            vpc = vpc,
            instance_name="bastion",
        )
