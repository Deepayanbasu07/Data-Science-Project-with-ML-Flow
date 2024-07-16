import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'Project_DS'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py",
   


] 

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, file_name = os.path.split(file_path)
    
    if filedir != "":
        os.makedirs(file_path, exist_ok= True)
        logging.info(f"Creating directory; {filedir} for the file: {file_name}")
        
    if (not os.path.exists(file_name)) or (os.path.getsize(file_name) == 0):
        with open(file_name, "w") as f:
            pass
            logging.info(f"Creating empty file: {file_name}")


    else:
        logging.info(f"{file_name} is already exists")