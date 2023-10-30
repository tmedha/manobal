from body import creds, add_cred, remove_cred

def test():
    print("Testing 1 2 3.")

    add_cred('windows', 'paramsiddharth', 'lallupassword123')
    remove_cred('windows')
    print(creds)

if __name__ == '__main__':
    test()