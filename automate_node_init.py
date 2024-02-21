import os
import shutil
from pathlib import Path


def change_directory(path):
    os.chdir(path)

# def list_directory():
#     os.system("dir")
def make_project_folder(name):
    os.system(f"mkdir {name}")

# def create_index_file(name):
#     # Content of the index.js file
#     content = """
# // index.js
# // init express
# const express = require('express');
# const app = express();
#
# // use dotenv to secure the environment variables
# require('dotenv').config();
# const port = process.env.PORT;
#
# // use cors to allow requests from the frontend
# const cors = require('cors');
# app.use(cors({
#     origin: '*'
# }));
#
# // use body-parser to parse the request body
# const bodyParser = require('body-parser');
# app.use(bodyParser.json({ limit: '50mb' }));
#
#
# // init database connection
# const initConnection = require('./DB/config');
# initConnection();
#
# // use the routes
# const {userRoutes, taskRoutes} = require('./src/routes/routes');
# app.use('/user', userRoutes);
# app.use('/task', taskRoutes);
#
#
# app.get('/', (req, res) => {res.json({message: 'TO-DO app listening'})})
#
#
# app.listen(port, () => console.log('{name} app listening on port ' + port +'!'))
#
#
# """
#
#     # Write content to index.js file
#     with open("index.js", "w") as file:
#         file.write(content)
#
#     print("index.js file created successfully!")

def init_npm_and_download_packages():
    os.system("npm init -y")
    os.system("npm i express mongoose bcryptjs body-parser cors dotenv jsonwebtoken nodemailer nodemon "
              "express-validator")


def copy_folders(source_folders, destination_path):
    # Assuming source_folders is a single path
    for folder in source_folders.iterdir():
        source = os.path.join(folder)
        destination = os.path.join(destination_path, os.path.basename(folder))
        if folder.is_file():
            try:
                shutil.copy(source,destination)
                print(f"Folder '{folder}' copied successfully to '{destination}'")
            except Exception as e:
                print(f"Error copying folder '{folder}': {e}")

        else:
            try:
                shutil.copytree(source, destination)
                print(f"Folder '{folder}' copied successfully to '{destination}'")
            except Exception as e:
                print(f"Error copying folder '{folder}': {e}")

if __name__ == "__main__":
    path = input("Enter the path: ")
    project = input("Enter project name:")
    
    change_directory(path)
    make_project_folder(project)
    change_directory(project)

    fullPath = os.path.join(path,project)
    srcPath = Path("F:\\be_sample\\")
    copy_folders(srcPath,fullPath)

    # create_index_file()
    init_npm_and_download_packages()

