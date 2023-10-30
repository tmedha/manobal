from body import creds, add_cred

def test():
    print("Testing 1 2 3.")

    add_cred('windows', 'paramsiddharth', 'lallupassword123')
    print(creds)
    #expected_output = {
    #  "windows": {
     #     "username": "paramsiddharth",
      #    "password": "lallupassword123"
      #}
    #}

if __name__ == '__main__':
    test()