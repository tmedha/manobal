from body import creds, add_cred, remove_cred, is_cred_present, save_creds

def test():
    print("Testing 1 2 3.")

    add_cred('windows', 'paramsiddharth', 'lallupassword123')
    remove_cred('windows')
    print(is_cred_present('windows'))
    save_creds()

if __name__ == '__main__':
    test()