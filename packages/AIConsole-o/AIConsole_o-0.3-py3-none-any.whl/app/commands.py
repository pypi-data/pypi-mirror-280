from colorama import init, Fore, Style


def help():
    help_text = (
            f"{Fore.GREEN}Welcome to the CLI Tool!{Style.RESET_ALL}\n\n"
            f"{Fore.YELLOW}Usage:{Style.RESET_ALL}\n"
            f"{Fore.CYAN}[command] [options]{Style.RESET_ALL}\n\n"
            f"{Fore.YELLOW}Available Commands:{Style.RESET_ALL}\n"
            f"{Fore.CYAN}help{Style.RESET_ALL}     - Displays this help message.\n"
            f"{Fore.CYAN}list{Style.RESET_ALL}     - Lists available items.\n"
            f"{Fore.CYAN}create{Style.RESET_ALL}   - Creates a new item.\n"
            f"{Fore.CYAN}delete{Style.RESET_ALL}   - Deletes an existing item.\n\n"
            f"{Fore.YELLOW}Options:{Style.RESET_ALL}\n"
            f"{Fore.CYAN}-v, --verbose{Style.RESET_ALL}  - Increase output verbosity.\n"
            f"{Fore.CYAN}-h, --help{Style.RESET_ALL}   - Show this help message and exit.\n\n"
            f"{Fore.YELLOW}Examples:{Style.RESET_ALL}\n"
            f"{Fore.CYAN}list -v{Style.RESET_ALL}    - List available items with verbose output.\n"
            f"{Fore.CYAN}create --name 'New Item'{Style.RESET_ALL} - Create a new item named 'New Item'.\n\n"
            f"{Fore.YELLOW}For more information on specific commands, use:{Style.RESET_ALL}\n"
            f"{Fore.CYAN}help [command]{Style.RESET_ALL}\n\n"
            f"{Fore.GREEN}Enjoy using the CLI Tool!{Style.RESET_ALL}"
        )
    print(help_text)