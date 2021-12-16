import urllib.request
import datetime
from cloudwatch_metrics import CloudWatchMetric
import constants as constants

def lambda_handler(events, context):
    values = dict()
    URL = "https://stackoverflow.com"
    dimensions = [{'Name':'URL', 'Value':URL},
                    {'Name':'Region', 'Value':'US'}]
    cw = CloudWatchMetric()
    
    avail = get_avail(URL)
    cw.put_data(constants.URL_MONITOR_NAMESPACE,
                constants.URL_MONITOR_NAME_AVAILIBILITY,
                dimensions,
                avail)
    
    latency = get_latency(URL)
    cw.put_data(constants.URL_MONITOR_NAMESPACE,
                constants.URL_MONITOR_NAME_LATENCY,
                dimensions,
                latency)
    
    values.update({'availibility':avail, 'latency':latency})
    return values
    
def get_avail(url):
    if urllib.request.urlopen(url).getcode() == 200:
        return 1
    else:
        return 0

def get_latency(url):
    start = datetime.datetime.now()
    response = urllib.request.urlopen(url)
    end = datetime.datetime.now()
    delta = start - end
    return round(delta.microseconds * 10**-6, 6)
    