import requests
import urllib3
from requests.auth import HTTPBasicAuth
import pprint
pp =pprint.PrettyPrinter
urllib3.disable_warnings()

# Get Authentication token
def get_dnac_jwt_token():
    response = requests.post(BASE_URL + AUTH_URL,
                             auth=HTTPBasicAuth("devnetuser", "Cisco123!"),
                             verify=False)
    token = response.json()['Token']
    return token

# Get client health
token = get_dnac_jwt_token()
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}

def get_client_health(headers):
    response = requests.get(BASE_URL + CLIENT_HEALTH,
                            headers=headers, verify=False)
    return response.json()['response']

def main():
    # obtain the Cisco DNA Center Auth Token
    token = get_dnac_jwt_token()
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}

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