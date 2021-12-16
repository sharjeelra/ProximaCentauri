import boto3
from resources import constants as constants

class CloudWatchMetric:
    def __init__(self):
        self.client = boto3.client('cloudwatch')    
    
    def put_data(self, namespace, metric_name, dimensions, value):
        response = self.client.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'metric_name':metric_name,
                    'dimensions':dimensions,
                    'value':value
                }])