import json
from cryptography.fernet import Fernet

creds = {}

storage_file = 'creds.manobal'

key = Fernet.generate_key()

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
    key_object = Fernet(key)
    encrypted_credentials = key_object.encrypt(string.encode())
    return encrypted_credentials


def decrypt_creds(encrypted_credentials, key):
    key_object = Fernet(key)
    decrypted_creds = key_object.decrypt(encrypted_credentials).decode()
    return decrypted_creds