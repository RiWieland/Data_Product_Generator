import os
import logging
from config.config_simulation import PATH_SOURCE

def create_source_dir(path_list: list):
    """
    creates the dir for the source for the simulation
    """
    for path in path_list:
        try:
            os.mkdir(path)
            logging.info(f"Directory '{path}' created successfully.")
        except FileExistsError:
            logging.info(f"Directory '{path}' already exists.")
            continue
