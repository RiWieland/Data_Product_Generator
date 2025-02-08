import os
import logging
from config.config_simulation import PATH_SOURCE

def create_source_dir(path: str):
    """
    creates the dir for the source for the simulation
    """
    os.mkdir(path)
    logging.info(f"Directory '{path}' created successfully.")


