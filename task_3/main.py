import sys, os
from pathlib import Path
from colorama import Fore, Back, Style

def parseFolder(path: str, deep: int = 1):
    directory = Path(path)
    if not directory.is_dir():
        print(f"{Fore.RED}{Style.BRIGHT}Error: incorrect path{Style.RESET_ALL}")
        return False

    tab = '  ' * deep

    if deep == 1:
        print(f"{Fore.BLUE}{Style.BRIGHT}{path}/{Style.RESET_ALL}")

    for node in directory.iterdir():
        p_node = Path(node)
        relative_path = p_node.relative_to(path)

        if p_node.is_dir():
            print(f"{tab}{Fore.BLUE}{Style.BRIGHT}{relative_path}/{Style.RESET_ALL}")
            parseFolder(node, deep + 1)
        elif p_node.is_symlink():
            target = os.readlink(node)
            print(f"{tab}{Fore.CYAN}{node} -> {target}{Fore.RESET}")
        elif p_node.is_file():
            print(f"{tab}{Fore.LIGHTGREEN_EX}{relative_path}{Fore.RESET}")
        else:
            print(f"{tab}Unknown: {node}")


def main():
    if len(sys.argv) > 1:
        parseFolder(sys.argv[1])

if __name__ == "__main__":
    main()
