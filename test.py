from body import creds, add_cred, remove_cred, is_cred_present, load_creds, encrypt_creds, decrypt_creds, string_to_key, ensure_creds
from cryptography.fernet import Fernet
import json
from pprint import pp

def test():
    key = 'abc'
    key_final = string_to_key(key)
    # print(key_final)
    # print("Testing 1 2 3.")
    ensure_creds(key_final)
    load_creds(key_final)
    # add_cred('windows', 'paramsiddharth', 'lallupassword123', key_final)
    # add_cred('Microsoft', 'Medha', 'password', key_final)
    # remove_cred('windows', key_final)
    # # remove_cred('Microsoft', key_final)
    # print(is_cred_present('windows'))
    pp(creds)
    # aes ka prayog kuchh fernet and cyrptography library falana dh
    # string_creds = 'Hello'
    key_check = Fernet(key_final)
    # encrypted = encrypt_creds(string_creds, key)
    # print(encrypted)
    # decrypted = decrypt_creds(encrypted, key)
    # print(decrypted)

if __name__ == '__main__':
    test()