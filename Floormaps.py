# Modules import
from Authentication import *
import pprint
my_printer = pprint.PrettyPrinter(indent=1, width=90, depth=3)
import urllib3
urllib3.disable_warnings()


# Base URL setup to create dynamic strings for more specific endpoints
BASE_URL = 'https://sandboxdnac.cisco.com'

# Endpoint URLs
FLOOR_URL =  "/dna/intent/api/v1/wireless/floormap/all"

# Get Authentication token
token = get_dnac_jwt_token()

# Get site health
def get_FLOOR(headers):
    response = requests.request('GET', BASE_URL + FLOOR_URL,
                            headers=headers, verify=False)
    return response

def main():
    # obtain the Cisco DNA Center Auth Token
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}

    # Retrieving and printing floormap
    print('Getting floormap...')
    response = get_FLOOR(headers)
    floormaps = response
    for floor in floormaps
        if
    print(response)

if __name__ == "__main__":
    main()