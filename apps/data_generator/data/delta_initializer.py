"""
Initialize the Delta files use for the load
"""
from apps.config.config_simulation import PATH_DOCKER_SINK
from simulation.abstract.abstract_table import DataTable
from pyspark.sql import SparkSession
from delta.tables import DeltaTable

from utils.utils import get_spark


class DeltaInitializer:
    """
    A class to create data artificially
    """

    def __init__(self, table:DataTable, path_:str = None, spark:SparkSession = get_spark()):
        self.table = table
        self.path = self._get_path(path_)
        self.spark = spark
        self._is_delta_initialized = self.delta_exists()

    def _get_path(self, path_) -> str:
        """
        create the default path
        """
        if path_ is not None:
            target_path = path_
        else:
            target_path= PATH_DOCKER_SINK + self.table.name
        return target_path

    def delta_exists(self) -> bool:
        """
        function checks if in the specified path there is a delta file already initialized
        """
        if DeltaTable.isDeltaTable(self.spark, self.table.path):
            return True
        return False
