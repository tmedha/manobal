creds = {}

def add_cred(platform, username, password):
    creds[platform] = {"username": username, "password": password}

def remove_cred(platform) :
    del creds[platform]
    # creds.pop(platform)