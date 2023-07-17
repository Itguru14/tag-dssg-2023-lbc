# TAG-DSSG-2023-LBC_project

This repo will serve as the shared repo for us to collaborate on the LBC TAG summer project. 

This repo will contain code, dashboard artifacts, code snippets, documentation of deployed solutions
report of the entire project, presentation slides and all things related to the project. 

We will be using Google Colab and Tableau concurrently for the project as agreed to by team members.

find below a brief description of the main directories and files in this repo and their functions

/datapipelines      -   Intended to hold scripts for automating download of data from google drive\ \
/utilities -    various samples code, code snippets, images etc that will be necessary for the main analysis files\ \
.gitignore -      used to instruct git which files should be ignored when using git version control\
LBC_main.ipynb  - main file for the google colab analysis \



To use this repo it is recommended you create a fork of this repo and then make a clone of your fork to run some \
some of the codes locally in addition to using google colab to run the LBC_main.ipnyb file.


The first thing we need to accomplish is automate data transfer from google drive to local. Please see the folder "datapipelines" in the current repository for a script that
list all of the files and folder in your google drive by using a unique ID and lists ids and corresponding names for all files and folders in the google drive, you may then use the ID corresponding to any folder  or file to pull that folder or file from google drive using one of the python script in the datapipelines folder.

