from helpers import (
    create_user,
    login_user,
    update_user_email,
    delete_user,
    exit_program
)

def main():
    while True:
        print("\n Language Learning CLI")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Update Email")
        print("4. Delete Account")
        print("5. Exit")
        
        choice = input("> ")

        if choice == "1":
            create_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            update_user_email()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
