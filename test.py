from body import creds, add_cred, remove_cred, is_cred_present, load_creds, encrypt_creds, decrypt_creds
from cryptography.fernet import Fernet
import json
from pprint import pp

def test():
    # print("Testing 1 2 3.")
    # load_creds()
    # add_cred('windows', 'paramsiddharth', 'lallupassword123')
    # add_cred('Microsoft', 'Medha', 'password')
    # remove_cred('windows')
    # remove_cred('Microsoft')
    # print(is_cred_present('windows'))
    # pp(creds)
    #aes ka prayog kuchh fernet and cyrptography library falana dh
    string_creds = 'Hello'
    key = Fernet.generate_key()
    encrypted = encrypt_creds(string_creds, key)
    print(encrypted)
    decrypted = decrypt_creds(encrypted, key)
    print(decrypted)

if __name__ == '__main__':
    test()