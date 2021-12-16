from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class PCappStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
        mylambda = self.create_lambda('WebHealthLambda', './resources', 'web_health.lambda_handler')
        
    def create_lambda(self, id, asset, handler):
        return lambda_.Function(self, id = id,
            runtime=lambda_.Runtime.PYTHON_3_6,
            handler=handler,
            code=lambda_.Code.from_asset(asset)
)
