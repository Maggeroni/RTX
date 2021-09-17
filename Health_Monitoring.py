# Modules import
from Authentication import *
import pprint
pp = pprint.PrettyPrinter()

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()

# Base URL setup to create dynamic strings for more specific endpoints
BASE_URL = 'https://sandboxdnac.cisco.com'

# URLs
SITE_HEALTH = '/dna/intent/api/v1/site-health'
NETWORK_HEALTH = '/dna/intent/api/v1/network-health'
CLIENT_HEALTH = '/dna/intent/api/v1/client-health'

# Get Authentication token
token = get_dnac_jwt_token()

# Get site health
def get_site_health(headers):
    response = requests.get(BASE_URL + SITE_HEALTH,
                            headers=headers, verify=False)
    return response.json()['response']

# Get network health
def get_network_health(headers):
    response = requests.get(BASE_URL + NETWORK_HEALTH,
                            headers=headers, verify=False)
    return response.json()['response']

# Get client health
def get_client_health(headers):
    response = requests.get(BASE_URL + CLIENT_HEALTH,
                            headers=headers, verify=False)
    return response.json()['response']


def main():
    # obtain the Cisco DNA Center Auth Token
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}

    # Site health
    print('Printing site health...')
    response = get_site_health(headers)
    for site in response:
        print('Site: {0}, Health: {1}'.format(site['siteName'], site['networkHealthAverage']))

    # Network health
    print('\nPrinting network health...')
    response = get_network_health(headers)
    print('Good: {0}, Bad: {1}, Health score: {2}'.format(
        response[0]['goodCount'], response[0]['badCount'],
        response[0]['healthScore']
    ))

    # Client health
    print('\nPrinting client health...')
    response = get_client_health(headers)
    for score in response[0]['scoreDetail']:
        print('Type: {0}, Count: {1}, Score: {2}'.format(
            score['scoreCategory']['value'],
            score['clientCount'], score['scoreValue']))
        try:
            for category in score['scoreList']:
                print('\tType: {0}, Count: {1}'.format(
                    category['scoreCategory']['value'],
                    category['clientCount']))
        except:
            pass

if __name__ == "__main__":
    main()