import os
import luacrush
import time
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def remove_pycache():
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")

def main():
    print(bcolors.HEADER + "=== Welcome to LunaCrush - the Lua minifier/compressor! ===" + bcolors.ENDC + "\n")

    while True:
        print("Menu:")
        print("1. Minify a Lua script")
        print("2. Quit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            file_path = input("Please enter the full path of the Lua script you want to minify: ")

            if not os.path.isfile(file_path):
                print(bcolors.FAIL + "Error - File not found!" + bcolors.ENDC + "\n")
                continue

            try:
                print("Minifying the Lua script...")
                for _ in range(5):
                    print(".", end='', flush=True)
                    time.sleep(0.5)
                print()

                luacrush.compress_lua(file_path)
                print(bcolors.OKGREEN + "Lua script has been successfully minified!" + bcolors.ENDC + "\n")

            except Exception as e:
                print(bcolors.FAIL + "An error occurred during minification:", e, bcolors.ENDC, "\n")

        elif choice == '2':
            remove_pycache()
            print(bcolors.WARNING + "Exiting LunaCrush. Goodbye!" + bcolors.ENDC)
            break

        else:
            print(bcolors.WARNING + "Invalid choice. Please try again." + bcolors.ENDC + "\n")

if __name__ == "__main__":
    main()
