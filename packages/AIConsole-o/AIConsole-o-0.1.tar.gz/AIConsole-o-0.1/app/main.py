import google.generativeai as genai
import os
import time
import sys
from dotenv import load_dotenv
from colorama import init, Fore, Style

# Files
from app.logo import *
from app.api import *
from app.commands import *
from app.prompts import *
from app.os_system import *



def initialize_model():
    # Get the API key from environment variables
    API_KEY = os.getenv("API_KEY")

    # Configure the generative AI model
    genai.configure(api_key=API_KEY)

    # Initialize the model
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat_model = genai.GenerativeModel('gemini-1.5-flash')
    chat = chat_model.start_chat(history=[])
    
    return chat

chat = initialize_model()

def objective():
    objective_array = Personality()
    try:
        response = chat.send_message(objective_array)
        return response.text
    except genai.types.generation_types.StopCandidateException as e:
        print("Error: The response could not be generated due to safety concerns. Please try again with a different prompt.")

def generate_response(prompt):
    full_prompt = (
        "You are currently interacting with a user through a command-line interface (CLI) terminal.\n\n"
        "Below is the input prompt provided by the user:\n"
        + prompt
    )

    print(Fore.YELLOW + "Generating response...\n")
    #start_time = time.time()
    try:
        response = chat.send_message(full_prompt)
        #end_time = time.time()
        #elapsed_time = (end_time - start_time)
        #print(Fore.GREEN + "Response generated in {:.2f} ms".format(elapsed_time))
        print(Fore.GREEN + "  " + response.text)
    except genai.types.generation_types.StopCandidateException as e:
        print("Error: The response could not be generated due to safety concerns. Please try again with a different prompt.")


def main():
    # Initialize colorama to work with ANSI escape sequences on Windows
    init(autoreset=True)
    # Load environment variables from the .env file
    load_dotenv()
    display_logo()
    check_api_key()
    usage_instructions()
    objective()
    while True:
        prompt = input(Fore.WHITE + 'What can I help you find today? ' + Fore.WHITE)
        words = prompt.split()
        if prompt.lower() == "off":
            print(Fore.YELLOW + 'Hope we see you again\n')
            break
        elif prompt.lower() == 'display_system_info' or prompt.lower() == 'display_system_info()':
            print('\n')
            display_system_info()
            print('\n')
        elif len(words) > 0 and words[0].lower() == "@":
            generate_response(prompt)
        else:
            os.system(prompt)

if __name__ == "__main__":
    main()
