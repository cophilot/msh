import os
import sys

ERROR_LOG = []
FUNCTION_NAMES = []
print("Checking function naming...")


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: function-naming-check <dir>")
        sys.exit(1)

    dir_name = args[0]
    check_dir(dir_name)

    if len(ERROR_LOG) == 0:
        sys.exit(0)
        print("Done")

    print("")
    print(f"{len(ERROR_LOG)} Errors found:")
    for error in ERROR_LOG:
        print(error)

    sys.exit(1)


def check_dir(dir_name):
    for root, _, files in os.walk(dir_name):
        for file in files:
            print(f"Checking {file}...")
            with open(os.path.join(root, file)) as f:
                lines = f.readlines()
                line_before = None
                line_number = 1
                for line in lines:
                    check_line(line, line_before, os.path.join(root, file), line_number)
                    line_before = line
                    line_number += 1


def check_line(line, line_before, file_path, line_number):
    line = line.strip()
    if line.startswith("function ") and line.endswith("{"):
        function_name = (
            line.replace(" ", "")
            .replace("function", "")
            .replace("{", "")
            .replace("(", "")
            .replace(")", "")
        )
        check_duplicated_function_name(function_name, file_path, line_number)
        check_snake_case(function_name, file_path, line_number)
        check_function_comment(function_name, line_before, file_path, line_number)


def check_function_comment(function_name, line_before, file_path, line_number):
    if line_before is None:
        return
    if not line_before.startswith("#"):
        ERROR_LOG.append(
            f"Missing Function comment: {function_name} ({file_path}:{line_number})"
        )


def check_snake_case(function_name, file_path, line_number):
    if not function_name.islower():
        ERROR_LOG.append(
            f"Function name is not snake case: {function_name} ({file_path}:{line_number})"
        )


def check_duplicated_function_name(function_name, file_path, line_number):
    if function_name in FUNCTION_NAMES:
        ERROR_LOG.append(
            f"Duplicate function name found: {function_name} ({file_path}:{line_number})"
        )
    else:
        FUNCTION_NAMES.append(function_name)


if __name__ == "__main__":
    main()
