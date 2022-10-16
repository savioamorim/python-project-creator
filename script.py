import os

# Templates Path
MAIN_TEMPLATE_PATH = "./templates/main.txt"
GIT_IGNORE_TEMPLATE_PATH = "./templates/git_ignore.txt"
FIRST_TEST_TEMPLATE_PATH = "./templates/first_test.txt"
LAUNCH_TEMPLATE_PATH = "./templates/launch.txt"
FIRST_CLASS_TEMPLATE_PATH = "./templates/first_class.txt"
SETTINGS_TEMPLATE_PATH = "./templates/settings.txt"


def build_template(template_path, file_path):
    template = open(template_path, "r", encoding="utf-8")
    open(file_path, "w", encoding="utf-8").write(template.read())


# Creating folder structure
os.mkdir("./src")
os.mkdir("./test")
os.mkdir("./.vscode")

# Creating templates files
build_template(MAIN_TEMPLATE_PATH, "./main.py")
build_template(GIT_IGNORE_TEMPLATE_PATH, "./.gitignore")
build_template(FIRST_TEST_TEMPLATE_PATH, "./test/test_template.py")
build_template(LAUNCH_TEMPLATE_PATH, "./.vscode/launch.json")
build_template(SETTINGS_TEMPLATE_PATH, "./.vscode/settings.json")
build_template(FIRST_CLASS_TEMPLATE_PATH, "./src/my_first_class.py")

os.system("python3 -m venv venv")

# Updating pip
os.system('./venv/bin/python3 -m pip install --upgrade pip')

# Installing basic dependencies
os.system('./venv/bin/python3 -m pip install -U autopep8')
os.system('./venv/bin/python3 -m pip install -U pylint')

# TODO Activating python environment
