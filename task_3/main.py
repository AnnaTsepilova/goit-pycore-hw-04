import sys
from pathlib import Path
from colorama import Fore, Back, Style

def parseFolder(path: str):
    print(path)


def main():
    if len(sys.argv) > 1:
        parseFolder(sys.argv[1])

if __name__ == "__main__":
    main()
