import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
    )

PROJECT_NAME = "cli_project" # "<PROJECT_NAME>"
REPO_NAME = "python-cli-template" # "<REPO_NAME>"
AUTHOR_USER_NAME = "c17hawke" # "<AUTHOR_USER_NAME>"
PACKAGE_NAME = "my_cli" # "<PACKAGE_NAME>"
AUTHOR_EMAIL = "sunny.c17hawke@gmail.com" # "<AUTHOR_EMAIL>"
COMMAND_NAME = PACKAGE_NAME # "<COMMAND_NAME>"
SITE_AUTHOR = AUTHOR_USER_NAME # "<SITE_AUTHOR>"

logging.info(f"Creating project by name: {PROJECT_NAME}")

# list of files:
list_of_files = [
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/cli.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    f"research/trial_001.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")

class UpdateContent:
    def __init__(self, path: str, **kwargs):
        self.path = path
        self.kwargs = kwargs

    def read_content(self):
        with open(self.path, "r") as f:
            self.content = f.read()
        if self.content!= "":
            logging.info(f"content read succesfully from: {self.path}")

    def update_content(self):
        if self.content!= "":
            for key, value in self.kwargs.items():
                self.content = self.content.replace(f"<{key}>", value)
            logging.info(f"content replaced succesfully!")

    def write_content(self):
        if self.content != "":
            with open(self.path, "w") as f:
                f.write(self.content)
            logging.info(f"content updated succesfully and written to: {self.path}")

path_and_kwargs = {"setup.py":{
    "REPO_NAME": REPO_NAME,
    "AUTHOR_USER_NAME": AUTHOR_USER_NAME,
    "PACKAGE_NAME": PACKAGE_NAME,
    "AUTHOR_EMAIL": AUTHOR_EMAIL,
    "COMMAND_NAME": COMMAND_NAME
    },
    "mkdocs.yml": {
    "PACKAGE_NAME": PACKAGE_NAME, 
    "SITE_AUTHOR": SITE_AUTHOR
    },
    "setup.cfg": {
    "PACKAGE_NAME": PACKAGE_NAME
    } 
    }

for path, kwargs in path_and_kwargs.items():
    update_content = UpdateContent(path=Path(path), **kwargs)
    update_content.read_content()
    update_content.update_content()
    update_content.write_content()
