from colorama import init, Fore, Style
import sys
import os

def display_logo():
    logo = f"""
{Fore.CYAN}

    
                                                                                                          
 @@@@@@   @@@   @@@@@@@   @@@@@@   @@@  @@@   @@@@@@    @@@@@@   @@@       @@@@@@@@              @@@@@@   
@@@@@@@@  @@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@   @@@@@@@@  @@@       @@@@@@@@             @@@@@@@@  
@@!  @@@  @@!  !@@       @@!  @@@  @@!@!@@@  !@@       @@!  @@@  @@!       @@!                  @@!  @@@  
!@!  @!@  !@!  !@!       !@!  @!@  !@!!@!@!  !@!       !@!  @!@  !@!       !@!                  !@!  @!@  
@!@!@!@!  !!@  !@!       @!@  !@!  @!@ !!@!  !!@@!!    @!@  !@!  @!!       @!!!:!    @!@!@!@!@  @!@  !@!  
!!!@!!!!  !!!  !!!       !@!  !!!  !@!  !!!   !!@!!!   !@!  !!!  !!!       !!!!!:    !!!@!@!!!  !@!  !!!  
!!:  !!!  !!:  :!!       !!:  !!!  !!:  !!!       !:!  !!:  !!!  !!:       !!:                  !!:  !!!  
:!:  !:!  :!:  :!:       :!:  !:!  :!:  !:!      !:!   :!:  !:!   :!:      :!:                  :!:  !:!  
::   :::   ::   ::: :::  ::::: ::   ::   ::  :::: ::   ::::: ::   :: ::::   :: ::::             ::::: ::  
 :   : :  :     :: :: :   : :  :   ::    :   :: : :     : :  :   : :: : :  : :: ::               : :  :   
                                                                                                                                                                                                                                                                                                                                                         
   
{Style.RESET_ALL}
"""
    
    print(logo)
    print(Fore.CYAN + 'Welcome to Ada CLI - Your Friendly AI Assistant \n')
    print(Fore.YELLOW + 'Created BY - Houssam-nxy - https://github.com/Houssam-nxy\n')


        
def usage_instructions():
    print(Fore.WHITE + "Usage instructions:\n")
    print(Fore.YELLOW + "- Type commands directly for system operations or general queries.")
    print(Fore.YELLOW + "- To interact with the AI, start your input with " + Fore.RED + "'@ '" + Fore.YELLOW + " followed by your query.")
    print(Fore.YELLOW + "- To exit Ada CLI, type " + Fore.RED + "'off'" + Fore.YELLOW + " and press Enter.\n")
