import os 
from pathlib import Path
import logging 
logging.basicConfig(level=logging.INFO,format='[%(asctime)s:%(message)s:]')

project_name="cnnclassifier"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/steps/__init__.py",
    f"src/{project_name}/constants/steps/step.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "research/trails.ipynb",
    "setup.py",
    "templates/index.html"

    
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory;{filedir} for the file:{filename}")


    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
           with open(filepath,"w")as f:
                pass
                logging.info(f"creating empty file:{filepath}")




    else:
        logging.info(f"{filename} is already exists")             