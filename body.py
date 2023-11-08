import json

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

def view_credentials(view_platform_creds):
    # print(creds[platform])
    # view_platform_creds = input('Enter the platform you want to view: ')
    if is_cred_present(view_platform_creds):
        view_username = creds[view_platform_creds]['username']
        view_password = creds[view_platform_creds]['password']
        print(f'Username: {view_username}')
        print(f'Password: {view_password}')
    else:
        print('Platform ',view_platform_creds, 'not found.')

def view_all_credentials(view_platform_creds):
    ...

    # for platform in creds:
        # print('Platform: ', platform,'\n', creds[platform])