#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from aws_cdk.core import Tags

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from cdk_resources.cdk_resources_stack import CdkResourcesStack


app = core.App()
resources = CdkResourcesStack(app, "CdkResourcesStack", "192.168.0.0/21")

Tags.of(resources).add("project", "cdk-resources")
Tags.of(resources).add("environment", "testing")

app.synth()
