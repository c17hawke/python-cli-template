# python cli template

Documentation: https://c17hawke.github.io/<repo-name>/
project board - `<add project board link if any>`

## STEPS - 

### STEP 01: Create new repository using this template 

by choosing this as a project template while creating a new repository

### STEP 02: Clone the new repository or use codespaces

- To clone you can use the following command - 
    ```bash
    git clone https://github.com/c17hawke/<repo-name>
    ```
    NOTE: update the repo-name here

- Click on create code spaces or selec available codespaces as shown below - 
    image.png

### STEP 03: IMPORTANT: Create `.env` file in the root of the project and paste the following content - 

```ini
# update the following values as per your project
PROJECT_NAME="<YOUR_PROJECT_NAME>"
REPO_NAME="<YOUR_REPO_NAME>"
AUTHOR_USER_NAME="YOUR_<AUTHOR_USER_NAME>"
PACKAGE_NAME="<YOUR_PACKAGE_NAME>"
AUTHOR_EMAIL="<YOUR_AUTHOR_EMAIL>"
COMMAND_NAME="<YOUR_COMMAND_NAME>"
SITE_AUTHOR="<YOUR_SITE_AUTHOR>"
PYTHON_VERSION=3.8 # update as per your requirements
```

> **WARNING: if this step is skipped then exception will be raised**


### STEP 04: Run the template.py file

use template.py to create the other required files by running the following command - 

```bash 
python template.py
```

> This completes the basic skeleton of the project!!

### STEP 05: Create and install dependencies - 

- It is assumed that `anaconda` or `miniconda` is intalled in the system. If not then please do your setup by following this tutorial - https://youtu.be/bVM-QujJ0AI

- Update the `requirements_dev.txt` and `requirements.txt` files with the project requirements (i.e. required libraries)
- Now run the `init_setup.sh` file by running the following command - 
    ```bash
    bash init_setup.sh   
    ```
NOTE: if in case you face difficulty in running the init_setup.sh file then you can run the command mentioned in it one by one in the terminal to get the same result.

> This completes the environment setup of the project!!

> Now you can start the development!!!