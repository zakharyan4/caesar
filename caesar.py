import pyfiglet
from rich.console import Console

console = Console()
banner = pyfiglet.figlet_format("CAESAR")
console.print(f"[bold cyan]{banner}[/bold cyan]")

print("Welcome to Caesar!")

def get_mode():
    while True:
        try:
            mode = int(input("Choose the mode (1 or 2):\n 1. Decode with known key\n 2. Brute Force the key\n"))
            if mode not in (1, 2):
                raise ValueError("Choose 1 or 2!")
            return mode
        except ValueError as error:
            print(f"{error}")

def get_key():
    while True:
        try:
            shift_key = int(input("Please enter the key (from 1 to 25): "))
            if not (1 <= shift_key <= 25):
                raise ValueError("Invalid number. Try again!")
            return shift_key
        except ValueError as err:
            print(f"{err}")

def get_message():
    return input("Please enter the message to decrypt: ")

def rot(key, message):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result

def known_key():
    message = get_message()
    key = get_key()
    print(f"Decoded string is: {rot(-key, message)}")

def bruteforce():
    message = get_message()
    for key in range(1, 26):
        print(f"Key value: {key}, decoded:  {rot(-key, message)}")

def main():
    mode = get_mode()
    if mode == 1:
        known_key()
    else:
        bruteforce()

if __name__ == "__main__":
    main()
