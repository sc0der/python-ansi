import os
import sys
import subprocess

# Colors dictionary
COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}

def clear_terminal():
    if os.name == 'posix':  # Linux/Unix/Mac
        subprocess.call('clear', shell=True)
    elif os.name == 'nt':   # Windows
        subprocess.call('cls', shell=True)
    else:
        raise Exception("Cannot clear terminal. Unsupported operating system.")

def color_text(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

def main():
    clear_terminal()

    file_name = "text.txt" # default file name
    # get file name from the command line args
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    try:
        with open(file_name, "r") as f:
            ascii_art = f.read()
            print(color_text(ascii_art))
    except FileNotFoundError:
            print("Could not find the file " + file_name)

if __name__ == "__main__":
    main()
