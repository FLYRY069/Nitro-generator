import random
import string
import os
import requests
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_banner():
    banner = """
 _______  ___      __   __  _______  _______  __    _ 
|       ||   |    |  | |  ||       ||       ||  |  | |
|    ___||   |    |  |_|  ||    ___||    ___||   |_| |
|   |___ |   |    |       ||   | __ |   |___ |       |
|    ___||   |___ |_     _||   ||  ||    ___||  _    |
|   |    |       |  |   |  |   |_| ||   |___ | | |   |
|___|    |_______|  |___|  |_______||_______||_|  |__|
"""
    terminal_width = os.get_terminal_size().columns
    for line in banner.splitlines():
        print(line.center(terminal_width))


def static_animated_banner():
    animation = """
╔╦╗╦ ╦╔═╗╔╗╔╦╔═╔═╗  ╔═╗╔═╗╦═╗  ╦ ╦╔═╗╦╔╗╔╔═╗  ╔═╗╦ ╦ ╦       ╔═╗╔═╗╔╗╔
 ║ ╠═╣╠═╣║║║╠╩╗╚═╗  ╠╣ ║ ║╠╦╝  ║ ║╚═╗║║║║║ ╦  ╠╣ ║ ╚╦╝  ───  ║ ╦║╣ ║║║
 ╩ ╩ ╩╩ ╩╝╚╝╩ ╩╚═╝  ╚  ╚═╝╩╚═  ╚═╝╚═╝╩╝╚╝╚═╝  ╚  ╩═╝╩        ╚═╝╚═╝╝╚╝
"""
    clear_console()  
    terminal_width = os.get_terminal_size().columns
    lines = animation.strip().splitlines()
    
    for line in lines:
        print(line.center(terminal_width))
    time.sleep(1)  


def generate_code():
    code_length = random.randint(10, 12)  
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=code_length))
    return code


def check_code_legitimacy(code):
    discord_api_url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    
    
    response = requests.get(discord_api_url)
    
    
    return response.status_code == 200


def display_menu():
    while True:
        print("\nMenu:")
        print("1. Discord gift")
        print("2. Exit")
        
        choice = input("Please choose an option: ")

        if choice == "1":
            generate_codes()
        elif choice == "2":
            print("Exiting the program.")
            break  
        else:
            print("Invalid choice. Please try again.")


def generate_codes():
    valid_count = 0
    invalid_count = 0

    try:
        num_codes = int(input("\nHow many codes would you like to generate? "))
        static_animated_banner()  
        
        for _ in range(num_codes):
            code = generate_code()
            full_url = f"discord.gift/{code}"
            
            is_legit = check_code_legitimacy(code)

            
            if is_legit:
                valid_count += 1
                print(f"{full_url} | ✅ is valid")
            else:
                invalid_count += 1
                print(f"{full_url} | ❌ is invalid")

        
        if valid_count > 0:
            with open("valids.txt", "w") as f:
                f.write(f"Total valid codes: {valid_count}\n")

        
        print("\nResult:")
        print(f"Valid codes: {valid_count} | Invalid codes: {invalid_count}")
    
    except ValueError:
        print("Please enter a valid number.")


def main():
    clear_console()  
    display_banner()  
    display_menu()  


if __name__ == "__main__":
    main()



# made by flyry

# please dont skid :)
