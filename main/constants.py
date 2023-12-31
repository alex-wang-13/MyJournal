import os

""" Name of the user data folder. """
DATA_FOLDER_NAME: str = ".data"

""" The relative path from cwd to the CONSTS.txt folder. """
if not os.path.exists(DATA_FOLDER_NAME):
    os.makedirs(".data")
REL_CNSTS_PATH: os.PathLike = os.path.join(DATA_FOLDER_NAME, "CONSTS.txt")
if not os.path.exists(REL_CNSTS_PATH):
    with open(REL_CNSTS_PATH, "x") as file:
        pass

""" The global path to the constants file. """
USR_CNSTS_PATH: os.PathLike = os.path.join(os.getcwd(), REL_CNSTS_PATH)

""" The path to user-entered data. """
DATA_FOLDER_PATH: os.PathLike = os.path.join(os.getcwd(), DATA_FOLDER_NAME)