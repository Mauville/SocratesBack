import time

import requests

API_KEY = "n7q-kUdx6xN2_46V_HEQIPblxvgMJQjBDQyGkup_FXtv"
ACCOUNT = "55495ede-9b8a-466e-a626-c67d98f2ca9f-bluemix"


def get_access_token(api_key):
    """Retrieve an access token from the IAM token service."""
    token_response = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        data={
            "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
            "response_type": "cloud_iam",
            "apikey": api_key
        },
        headers={
            "Accept": "application/json"
        }
    )
    if token_response.status_code == 200:
        print "Got access token from IAM"
        print token_response.json()['access_token']
        return token_response.json()['access_token']
    else:
        print token_response.status_code, token_response.json()
        return None


def main(api_key, account):
    access_token = None
    while True:
        if not access_token:
            access_token = get_access_token(api_key)

        if access_token:
            response = requests.get(
                "https://{0}.cloudant.com/_all_dbs".format(
                    account),
                headers={
                    "Accept": "application/json",
                    "Authorization": "Bearer {0}".format(access_token)
                }
            )
            print "Got Cloudant response, status code", response.status_code
            if response.status_code == 401:
                print "Token has expired."
                access_token = None

        time.sleep(1)


if __name__ == "__main__":
    main(API_KEY, ACCOUNT)
