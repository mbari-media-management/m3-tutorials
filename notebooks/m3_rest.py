import datetime
import dateutil
import json
import pprint
import random
import requests
import urllib
import uuid

def show(s, data = None):
    "Display the json response from API calls"
    pp = pprint.PrettyPrinter(indent=2)
    print("--- " + s)
    if data:
      pp.pprint(data)
    
def iso8601():
    "Standardize the date format for pretty printing"
    return datetime.datetime.now(datetime.timezone.utc).isoformat()[0:-6] + "Z"

def auth_header(access_token):
    "Convience method to build JWT authorization header"
    return {"Authorization": "Bearer " + access_token}

def pretty_dict(d, indent=0):
    "Pretty print a python dictionary"
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
           pretty(value, indent+1)
        else:
           print('\t' * (indent+1) + str(value))
    
def parse_response(r):
    "Parse a JSON response"
    try:
       return json.loads(r.text)
    except:
        s = "URL: %s\n%s (%s): %s" % (r.request.url, r.status_code, r.reason, r.text)
        print(s)
        return {}
    
# --- Some helper functions that display the web traffic
#     Useful for demo
def pretty_print(pr):
    "Pretty print an HTTP request"
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------REQUEST-----------',
        pr.method + ' ' + pr.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in pr.headers.items()),
        pr.body,
    ))
    
def send(pr):
    pretty_print(pr)
    s = requests.Session()
    return s.send(pr)
     
def pretty_delete(url, access_token):
    r = requests.Request('DELETE', url, headers=auth_header(access_token))
    pr = r.prepare()
    return parse_response(send(pr))

def pretty_get(url):
    r = requests.Request('GET', url)
    pr = r.prepare()
    return parse_response(send(pr))

def pretty_post(url, access_token, data = {}):
    r = requests.Request('POST', url, data = data, headers=auth_header(access_token))
    pr = r.prepare()
    return parse_response(send(pr))

def pretty_put(url, access_token, data = {}):
    r = requests.Request('PUT', url, data = data, headers=auth_header(access_token))
    pr = r.prepare()
    return parse_response(send(pr))
    
    
# --- Basic REST calls, you'd probably use these in your own 
#     applications instead of the pretty-fied versions above. 
def delete(url, headers):
    return parse_response(requests.delete(url, headers=headers))

def get(url):
    return parse_response(requests.get(url))
    
def post(url, headers, data = {}):
    return parse_response(requests.post(url, data, headers=headers))

def put(url, headers, data = {}):
    return parse_response(requests.put(url, data, headers=headers))