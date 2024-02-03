import json
from cryptography.fernet import Fernet
import base64
import os
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib

creds = {}

storage_file = 'creds.manobal'

# key = Fernet.generate_key()

def add_cred(platform, username, password, key_byte):
    creds[platform] = {"username": username, "password": password}
    save_creds(key_byte)

def remove_cred(platform, key_byte) :
    del creds[platform]
    # creds.pop(platform)
    save_creds(key_byte)

def is_cred_present(platform):
    return platform in creds

def save_creds(key_byte):
    encoded_creds = json.dumps(creds)
    encrypted_creds = encrypt_creds(encoded_creds, key_byte)
    with open(storage_file, 'w', encoding = 'utf8') as creds_json:
        creds_json.write(encrypted_creds)

def load_creds(key_byte):
    with open(storage_file, 'r', encoding = 'utf8') as loading_creds_json:
        encrypted_creds_json = loading_creds_json.read()
        decrypted_creds = decrypt_creds(encrypted_creds_json, key_byte)
        updated_creds = json.loads(decrypted_creds)
        creds.update(updated_creds)

def ensure_creds(key_byte):
    if not os.path.isfile(storage_file):
        encoded_creds = json.dumps({})
        encrypted_creds = encrypt_creds(encoded_creds, key_byte)
        with open(storage_file, 'w', encoding = 'utf8') as creds_json:
            creds_json.write(encrypted_creds)

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

def encrypt_creds(string, key_byte):
    key_object = Fernet(key_byte)
    encrypted_credentials = key_object.encrypt(string.encode()).decode()
    return encrypted_credentials


def decrypt_creds(encrypted_credentials, key_byte):
    key_object = Fernet(key_byte)
    decrypted_creds = key_object.decrypt(encrypted_credentials.encode()).decode()
    return decrypted_creds

def string_to_key(key_string):
    key_byte = key_string.encode('utf-8')
    # salt = os.urandom(16)
    # kdf = PBKDF2HMAC(
    #     algorithm=hashes.SHA256(),
    #     length=32,
    #     salt=salt,
    #     iterations=390000,
    # )
    # key = base64.urlsafe_b64encode(kdf.derive(key_byte))
    hlib = hashlib.md5()
    hlib.update(key_byte)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))
    # return key