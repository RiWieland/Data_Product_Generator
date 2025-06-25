"""
Holder of the abstract table
"""
from abc import ABC, abstractmethod

from config.config_simulation import PATH_DOCKER_SINK
from utils.utils import get_spark


class DataTable(ABC):
    """
    Abstract class for Data Tables
    """

    def __init__(self, spark= get_spark()):
        self.spark = spark
        # self.path = self.create_default_path_runtime()
        self.path = self._default_landing_path_data_sink()
        # self.spark = get_spark()

    @property
    @abstractmethod
    def name(self):
        """
        Name of the table
        """

    def _module_to_path(self) -> str:
        """
        get dir of the object
        """
        root = str(self.__class__.__module__)
        relative_path = root.replace(".", "/")

        return relative_path

    def _default_landing_path_data_sink(self) -> str:
        """
        This function extracts the landing path for the data sink
        The idea is that all Data Products dirs are reassembling the structure in simulation
        """
        relative_path = str(self._module_to_path())
        path_tmp_list = relative_path.split("/")
        for i, obj in enumerate(path_tmp_list):
            if obj == 'simulation':
                ind = i
                break

        path = "/".join(path_tmp_list[ind+1:])
        path = PATH_DOCKER_SINK + str(path)
        return path

    def read_data(self):
        """
        method on the abstract class
        reads data on the associated delta file
        """
        df = self.spark.read.format("delta").load(self.path)
        return df
