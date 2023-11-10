import json
from cryptography import Fernet

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
    if is_cred_present(platform):
        view_username = creds[platform]['username']
        view_password = creds[platform]['password']
        print(f'Platform: {platform}')
        print(f'Username: {view_username}')
        print(f'Password: {view_password}')
    else:
        print('Platform {platform} not found.')

def view_all_credentials(platform):
    for platform in creds:
        view_username = creds[platform]['username']
        view_password = creds[platform]['password']
        print(f'• Platform: {platform}')
        print(f'  Username: {view_username}')
        print(f'  Password: {view_password}')
        print('')

def encrypt_creds(string, key):
    key = Fernet.generate_key()
    encryption_key = Fernet(key)
    encrypted_creds = {}
    for platform, values in creds.items():
        username = values['username'].encode('utf-8')
        password = values['password'].encode('utf-8')
        encrypted_username = encryption_key.encrypt(username)
        encrypted_password = encryption_key.encrypt(password)
        encrypted_creds[platform] = {
            'username': encrypted_username,
            'password': encrypted_password
        }
        with open('key.manobal', 'wb') as important_key:
            important_key.write(key)

        with open('encrypted_credentials.manobal', 'w') as encrypted_creds_file:
            json.dump(encrypted_creds, encrypted_creds_file)


def decrypt_creds(string, key):
    with open('key.manobal', 'rb') as important_key:
        key = important_key.read()
    with open('encrypted_credentials.json', 'r') as credentials_file:
        encrypted_credentials = json.load(credentials_file)