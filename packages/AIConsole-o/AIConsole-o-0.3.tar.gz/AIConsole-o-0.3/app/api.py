from colorama import init, Fore, Style
import sys
import os

def check_api_key():
    # File to store the API key
    api_key_file = 'api_key.txt'
    
    # Try to get the API key from the environment variable first
    api_key = os.environ.get('API_KEY')
    
    # If not found in the environment variables check the file
    if not api_key:
        if os.path.exists(api_key_file):
            with open(api_key_file, 'r') as file:
                api_key = file.read().strip()
    
    # Enter your api via input
    if not api_key:
        print(Fore.RED + "API key not found.")
        api_key = input("Please enter the API key: ")
        
        # Save the API key to the file
        with open(api_key_file, 'w') as file:
            file.write(api_key)
        print(Fore.GREEN + "API key has been saved to file.")
    
    # Set the API key in the environment variable for the current session
    os.environ['API_KEY'] = api_key
    print("API : " + Fore.GREEN + " ✓")