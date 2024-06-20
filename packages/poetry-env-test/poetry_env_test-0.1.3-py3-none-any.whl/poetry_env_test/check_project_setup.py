import os
import logging
import pkgutil
import sys


def check_dependencies(directories=None):
    if directories is None:
        # Get the current working directory
        current_dir = os.getcwd()
        directories = [
            os.path.join(current_dir, "src"),
            current_dir,
        ]

    logging.basicConfig(level=logging.INFO)
    for directory in directories:
        if not os.path.isdir(directory):
            logging.error("The directory %s does not exist.", directory)
            continue

        logging.info("Checking dependencies in directory %s", directory)
        for _, modname, ispkg in pkgutil.iter_modules([directory]):
            logging.info(
                "    Found module/submodule %s (is a package: %s)", modname, ispkg
            )


def print_python_path():
    print("\nCurrent PYTHONPATH:")
    for path in sys.path:
        if sys.path == "":
            print("    (empty)")
        print(path)


def check_env_info():
    print("\nPoetry Environment Info:")
    os.system("poetry env info")


if __name__ == "__main__":
    check_dependencies()
    print_python_path()
    check_env_info()
