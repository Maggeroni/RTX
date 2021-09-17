# Modules import
import requests
from Authentication import *
import pprint
my_printer = pprint.PrettyPrinter(indent=1, width=90, depth=4)
import urllib3
urllib3.disable_warnings()
import json

# Base URL setup to create dynamic strings for more specific endpoints
BASE_URL = 'https://sandboxdnac.cisco.com'

# Endpoint URLs
SITE_URL = "/dna/intent/api/v1/site"
SITE_TOPO_URL = "/dna/intent/api/v1/topology/site-topology"
PHY_TOPO_URL = url = "/dna/intent/api/v1/topology/physical-topology"

payload = None

# Get Auth Token
token = get_dnac_jwt_token()

#Get site
def get_site(headers):
    response = requests.request("GET", BASE_URL+SITE_URL, headers=headers, data=payload, verify=False)
    return response.json()['response']

# Get site topology
def get_site_topology(headers):
    response = requests.request("GET", BASE_URL + SITE_TOPO_URL, headers=headers, verify=False)
    return response.json()['response']

# Get physical topology
def get_phy_topology(headers):
    response = requests.request("GET", BASE_URL + PHY_TOPO_URL, headers=headers, verify=False)
    return response.json()['response']

def main():
    # obtain the Cisco DNA Center Auth Token
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json', "Accept": "application/json"}

    # Site Name
    print("Retrieving site names")
    # Get information about the sites
    response = json.dumps(get_site(headers))
    #print(response)
    # Define JSON data
    sitedata = response
    # Set key to search for in response
    keyVal = "name"
    # Load JSON data
    sites = json.loads(sitedata)
    # Search the key value using 'in' operator
    for site in sites:
        if keyVal in site:
            print("The site name is", site[keyVal])
        else:
            print("No sites found")

    # Site ID
    print("Retrieving site IDs")
    # Get information about the sites
    response = json.dumps(get_site(headers))
    # print(response)
    # Define JSON data
    sitedata = response
    # Set key to search for in response
    keyVal = "id"
    # Load JSON data
    sites = json.loads(sitedata)
    # Search the key value using 'in' operator
    for site in sites:
        if keyVal in site:
            print("The site id is", site[keyVal] )
        else:
            print("No site ids found")

    # Site topology
    print('Retrieving topology')
    response = get_site_topology(headers)
    print("Available sites are:",response)

    # Physical topology
    print("Retrieving physical topology")
    response = get_phy_topology(headers)
    my_printer.pprint(response)


if __name__ == "__main__":
    main()


