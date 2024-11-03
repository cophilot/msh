"""
compile all src files into a single script by getting the text from the files in src end 
extrating between '###START###' and '###END###' and 
writing them into the msh file ate the '###FUNCTIONS###' tag

Copy the content from the .phil-project into msh to store environment variables
"""

import sys
import os

OUT_FILE = "out/msh"
QUIET = False
TO_BINARY = False

MAIN_FILE = "src/main"
UTILS_DIR = "src/utils"
COMMANDS_DIR = "src/commands"
ENV_FILE = ".phil-project"
COMPILE_DEV_MODE = False


def main():
    """
    main function
    """

    set_args()

    log("Running the myshell compiler...")

    main_content = read_file(MAIN_FILE)

    main_content = inject_file(main_content, ENV_FILE, "###ENV###")
    main_content = inject_dir(main_content, COMMANDS_DIR, "###COMMANDS###")
    main_content = inject_dir(main_content, UTILS_DIR, "###UTILS###")
    if not COMPILE_DEV_MODE:
        main_content = remove_dev_mode_code(main_content)
    else:
        log("*Compiling in development mode*")
    # create the out directory if it does not exist
    base_dir = os.path.dirname(OUT_FILE)
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    write_out_file(main_content, OUT_FILE)
    make_file_executable(OUT_FILE)

    if TO_BINARY:
        make_binary(OUT_FILE)

    log("Compiled successfully: " + "\033[92m" + OUT_FILE + "\033[0m")
    log()


def inject_dir(
    main_content: str,
    dir_path: str,
    placeholder: str,
    with_bounds=True,
    start_bound="###START###",
    end_bound="###END###",
    only_return_content=False,
) -> str:
    """
    inject the content of the files in the directory into the main content
    """

    files = os.listdir(dir_path)
    result = ""

    for file in files:
        # if file is a directory recursively inject the content
        if os.path.isdir(dir_path + "/" + file):
            result += inject_dir(
                main_content,
                dir_path + "/" + file,
                placeholder,
                with_bounds,
                start_bound,
                end_bound,
                only_return_content=True,
            )
            continue
        if with_bounds:
            result += read_file_with_bounds(
                dir_path + "/" + file, start_bound, end_bound
            )
        else:
            result += read_file(dir_path + "/" + file)
    if only_return_content:
        return result
    return main_content.replace(placeholder, result)


def remove_dev_mode_code(content: str) -> str:
    """
    remove the dev mode code from the content
    """
    new_content = ""

    for line in content.split("\n"):
        if "###DEV-MODE###" in line:
            continue

        new_content += line + "\n"

    return new_content


def inject_file(
    main_content: str,
    file_path: str,
    placeholder: str,
    with_bounds=True,
    start_bound="###START###",
    end_bound="###END###",
) -> str:
    """
    inject the environment variables into the main content
    """
    result = ""
    if with_bounds:
        result = read_file_with_bounds(file_path, start_bound, end_bound)
    else:
        result = read_file(file_path)
    return main_content.replace(placeholder, result)


def make_file_executable(file: str):
    """
    make the file executable
    """
    os.system("chmod +x " + file)


def write_out_file(content: str, path: str):
    """
    write the content of the msh file into the out file
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def read_file_with_bounds(file_path: str, start: str, end: str):
    """
    read the file and get the content between the start and end bounds
    """
    content = read_file(file_path)

    new_content = ""

    in_bounds = False

    for line in content.split("\n"):
        if line.strip() == start:
            in_bounds = True
            continue
        if line.strip() == end:
            in_bounds = False
            continue
        if in_bounds:
            new_content += line + "\n"

    return new_content


def read_file(file_path: str):
    """
    read the main file and get the content
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: file not found: ", file_path)
    sys.exit(1)


def make_binary(file: str):
    """
    make the file a binary
    """
    # check if shc is installed
    if os.system("command -v shc > /dev/null") != 0:
        os.system("sudo apt-get install shc")
    os.system("shc -f " + file + " -o " + file + ".bin")
    os.system("rm " + file + ".x.c")
    os.system("rm " + file)
    os.system("mv " + file + ".bin " + file)


def set_args():
    """
    set the arguments for the command line
    """

    args = sys.argv

    for index, arg in enumerate(args):
        if arg == "-out" or arg == "-o":
            if index + 1 >= len(args):
                print("Error: no output file specified")
                sys.exit(1)

            global OUT_FILE
            OUT_FILE = args[index + 1]
        if arg == "-q" or arg == "-quiet":
            global QUIET
            QUIET = True
        if arg == "-b" or arg == "-binary":
            global TO_BINARY
            print("*Compiling to binary*")
            TO_BINARY = True
        if arg == "-h" or arg == "-help":
            print_help()
            sys.exit(0)
        if arg == "-dev-mode":
            global COMPILE_DEV_MODE
            COMPILE_DEV_MODE = True


def print_help():
    """
    print the help message
    """
    print("Usage: compile.py [options]")
    print()
    print("Options:")
    print("  -h, -help          print this help message")
    print("  -out, -o <file>    specify the output file")
    print("  -q, -quiet         run in quiet mode")
    print("  -b, -binary        compile to binary")
    print("  -dev-mode          compile in development mode")


def log(message: str = ""):
    """
    log the message
    """
    global QUIET
    if not QUIET:
        print(message)


if __name__ == "__main__":
    main()
