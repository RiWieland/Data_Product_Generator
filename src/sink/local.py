from config.config_simulation import PATH_SIMULATION


class WriteLocal:
    """
    the interface to write to the local test folder for the simulation
    """
    def __init__(self):
        self.path_simulation = PATH_SIMULATION

