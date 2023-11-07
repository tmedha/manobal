import json

creds = {}

storage_file = 'creds.manobal'

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
    encoded_creds = json.dumps(creds)
    with open(storage_file, 'w', encoding = 'utf8') as creds_json:
        creds_json.write(encoded_creds)

def load_creds():
    with open(storage_file, 'r', encoding = 'utf8') as loading_creds_json:
        encoded_creds_json = loading_creds_json.read()
        updated_creds = json.loads(encoded_creds_json)
        creds.update(updated_creds)

def display_platforms():
    print('Platforms: ')
    platforms = list(creds.keys())

    for list_platforms in platforms:
        print('•',list_platforms)

def view_credentials(platform):
    print(creds[platform])

def view_all_credentials():
    for platform in creds:
        print(creds[platform])