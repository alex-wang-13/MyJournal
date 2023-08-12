import os

""" The relative path from cwd to the CONSTS.txt file. """
os.makedirs(".data")
REL_CNSTS_PATH: os.PathLike = os.path.join(".data", "CONSTS.txt")

""" The global path to the constants file. """
USR_CNSTS_PATH: os.PathLike = os.path.join(os.getcwd(), REL_CNSTS_PATH)