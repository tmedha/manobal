from body import creds, add_cred, remove_cred, is_cred_present, load_creds

def test():
    print("Testing 1 2 3.")
    load_creds()
    print(creds)
    # add_cred('windows', 'paramsiddharth', 'lallupassword123')
    # add_cred('Microsoft', 'Medha', 'password')
    # remove_cred('windows')
    # print(is_cred_present('windows'))

if __name__ == '__main__':
    test()