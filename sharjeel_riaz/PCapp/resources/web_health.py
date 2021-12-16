import urllib.request
import datetime

def lambda_handler(events, context):
    values = dict()
    URL = "https://stackoverflow.com"
    avail = get_avail(URL)
    latency = get_latency(URL)
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
    