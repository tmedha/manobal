import json

creds = {}

def add_cred(platform, username, password):
    creds[platform] = {"username": username, "password": password}
    save_creds()

def remove_cred(platform) :
    del creds[platform]
    # creds.pop(platform)
    save_creds()

def is_cred_present(platform):
    return platform in creds

def save_creds():
    # credentials = "creds.manobal"
    encoded_creds = json.dumps(creds)
    with open('creds.manobal', 'w', encoding = 'utf8') as creds_json:
        creds_json.write(encoded_creds)