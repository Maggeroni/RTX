# Modules import
import requests
from requests.auth import HTTPBasicAuth

import pprint
pp = pprint.PrettyPrinter()

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()

# Authentication
BASE_URL = 'https://sandboxdnac.cisco.com'
AUTH_URL = '/dna/system/api/v1/auth/token'
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

# Get Authentication token
def get_dnac_jwt_token():
    response = requests.post(BASE_URL + AUTH_URL,
                             auth=HTTPBasicAuth(USERNAME, PASSWORD),
                             verify=False)
    token = response.json()['Token']
    return token

