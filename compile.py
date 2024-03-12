"""
compile all src files into a single script by getting the text from the files in src end 
extrating between '###START###' and '###END###' and 
writing them into the msh file ate the '###FUNCTIONS###' tag

Copy the content from the .phil-project into msh to store environment variables
"""

import sys
import os


OUT_FILE = "out/msh"

def main():
    """
    main function
    """
    set_args()
    msh_content = read_msh_file()
    write_out_file(msh_content)
    make_file_executable()

def make_file_executable():
    """
    make the file executable
    """
    os.system("chmod +x "+OUT_FILE)
    
def write_out_file(msh_content: str):
    """
    write the content of the msh file into the out file
    """
    # override the out file with the new content
    with open(OUT_FILE, "w", encoding="utf-8") as file:
        file.write(msh_content)

def read_msh_file():
    """
    read the msh file and get the content
    """
    try:
        with open("msh", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: msh file not found")
    except Exception as e:
        print("Error: ", e)
    sys.exit(1)


def set_args():
    """
    set the arguments for the command line
    """
    # get the command line arguments

    args = sys.argv

    for  index, arg in enumerate(args):
        if arg == "-out" or arg == "-o":
            if index+1 >= len(args):
                print("Error: no output file specified")
                sys.exit(1)

            global OUT_FILE
            OUT_FILE = args[index+1]

if __name__ == "__main__":
    main()
    