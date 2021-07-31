#This is script is automatically launched by cookiecutter after the launch

# remove the folder
import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


project_type_example = "{{cookiecutter.type}}" == "example"
project_type_simple = "{{cookiecutter.type}}" == "simple"

if project_type_example:
    # remove absolute path to file nested inside the generated folder
    remove(os.path.join(os.getcwd(), "lblocker.py"))
    remove(os.path.join(os.getcwd(), "logger.py"))

if project_type_simple:
    # remove relative file nested inside the generated folder
    remove(os.path.join("example"))
