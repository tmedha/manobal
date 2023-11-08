from body import add_cred, remove_cred, load_creds, is_cred_present, display_platforms, view_credentials, view_all_credentials
def main():
    print("Manobal actually sucks ngl.")
    #Likho welcome to manobal
    print('Hello everyone!\nWelcome to Manobal, your neighbourhood password manager which locally encrypts your credentials.')
    #List dikhao platforms ka
    while True:
        print('=====================================================================================================')
        load_creds()
        display_platforms()
        #Karna kya hai user (Add/Edit/Update, View, Delete)
        print('Choose what operation you would like to perform:')
        print('Press:\n1. For Adding/Updating a Credential.')
        print('2. For Deleting an Existing Credential.')
        print('3. For Viewing Existing Credentials.')
        print('4. Exit.\n')
        #User se number input karna hai
        choice = input("Enter your choice: ")

        if choice == '1':
            platform = input("Enter the platform for which you have credentials: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            add_cred(platform, username, password)
            # save_creds()

        elif choice == '2':
            platform_delete = input('Enter platform that you want to delete: ')
            if is_cred_present(platform_delete):
                remove_cred(platform_delete)
                print('Platform and linked credentials deleted.')
                # save_creds()
            else:
                print('Credential not found.')

        elif choice == '3':
            view_choice = input('Enter platform to view (enter A/All for viewing all): ')
            if is_cred_present(view_choice):
                view_credentials(view_choice)
            elif view_choice == 'All' or 'all' or 'A' or 'a':
                view_all_credentials(view_choice)
            else:
                print('Credential not found.')


        elif choice == '4':
            print('Now exiting. Goodbye!')
            break

        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main()