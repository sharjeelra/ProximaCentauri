from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_,
    aws_events as events_,
    aws_events_targets as targets_,
    aws_iam,
    aws_cloudwatch as cloudwatch,
)

class PCappStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        mylambda = self.create_lambda('WebHealthLambda', './resources', 'web_health.lambda_handler')
        
        # lambda_schedule = events_.Schedule.rate(cdk.Duration.minutes(1))
        # lambda_target = targets_.LambdaFunction(handler= mylambda)
        # rule = events_.Rule(self, "web_health_invocation", description="Periodic Lambda", 
                            # enabled=True, schedule=lambda_schedule, targets=[lambda_target])
        
    def create_lambda(self, id, asset, handler):
        return lambda_.Function(self, id = id,
            runtime=lambda_.Runtime.PYTHON_3_6,
            handler=handler,
            code=lambda_.Code.from_asset(asset)
)
