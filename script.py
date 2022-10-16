import os
import pip

# Templates Path
MAIN_TEMPLATE_PATH = "./templates/main.txt"
GIT_IGNORE_TEMPLATE_PATH = "./templates/git_ignore.txt"
FIRST_TEST_TEMPLATE_PATH = "./templates/first_test.txt"
LAUNCH_TEMPLATE_PATH = "./templates/launch.txt"
FIRST_CLASS_TEMPLATE_PATH = "./templates/first_class.txt"
SETTINGS_TEMPLATE_PATH = "./templates/settings.txt"

# Creating folder structure
os.mkdir("./src")
os.mkdir("./test")
os.mkdir("./.vscode")

# Creating main.py file
main_template = open(MAIN_TEMPLATE_PATH, "r")
file = open("./main.py", "w").write(main_template.read())

# Creating .gitignore file
gitignore_template = open(GIT_IGNORE_TEMPLATE_PATH, "r")
file = open("./.gitignore", "w").write(gitignore_template.read())

# Creating test.py file
first_test_template = open(FIRST_TEST_TEMPLATE_PATH, "r")
file = open("./test/test_template.py", "w").write(first_test_template.read())

# Creating launch.json file
launch_template = open(LAUNCH_TEMPLATE_PATH, "r")
file = open("./.vscode/launch.json", "w").write(launch_template.read())

# Creating settings.json file
settings_template = open(SETTINGS_TEMPLATE_PATH, "r")
file = open("./.vscode/settings.json", "w").write(settings_template.read())

# Creating first_class.py file
first_class_template = open(FIRST_CLASS_TEMPLATE_PATH, "r")
file = open("./src/my_first_class.py", "w").write(first_class_template.read())

# Creating python environment
os.system("python -m venv venv")

# TODO Activating python environment

# Updating pip
pip.main(["install", "--upgrade", "pip"])

# Installing basic dependencies
pip.main(["install", "-U", "autopep8"])
pip.main(["install", "-U", "pylint"])
