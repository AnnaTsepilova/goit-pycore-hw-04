import sys
import os
from pathlib import Path
from colorama import Fore, Style

def parse_folder(path: str, deep: int = 1):
    """
    Function scans directory and print internal items
    Function is recursive!
    """
    directory = Path(path)

    ## Check provided path
    if not directory.is_dir():
        print(f"{Fore.RED}{Style.BRIGHT}Error: folder path does not exist or not found{Style.RESET_ALL}")
        return False

    ## Tree indentation with spaces
    tab = '  ' * deep

    if deep == 1:
        print(f"{Fore.BLUE}{Style.BRIGHT}{path}/{Style.RESET_ALL}")

    ## Loop for folder items
    for node in directory.iterdir():
        p_node = Path(node)
        relative_path = p_node.relative_to(path)

        if p_node.is_dir():
            print(f"{tab}{Fore.BLUE}{Style.BRIGHT}{relative_path}/{Style.RESET_ALL}")
            parse_folder(node, deep + 1)
        elif p_node.is_symlink():
            target = os.readlink(node)
            print(f"{tab}{Fore.CYAN}{node} -> {target}{Fore.RESET}")
        elif p_node.is_file():
            print(f"{tab}{Fore.LIGHTGREEN_EX}{relative_path}{Fore.RESET}")
        else:
            print(f"{tab}Unknown: {node}")


def main():
    if len(sys.argv) > 1:
        parse_folder(sys.argv[1])
    else:
        print(f"  {Fore.BLUE}Usage: main.py FOLDER_TO_SCAN{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
