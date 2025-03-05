"""
write the dataframe in delta files in the sink
"""
from utils.utils import get_spark
from delta.tables import DeltaTable
from pyspark.sql import SparkSession, DataFrame


class DataWriter:
    """
    A class to create data artificially
    """

    def __init__(self, df:DataFrame, path:str, spark:SparkSession = get_spark()):
        self.df = df
        self.path = path
        self.spark = spark
        self._is_delta_initialized = self.delta_exists()

    def delta_exists(self) -> bool:
        """
        function checks if in the specified path there is a delta file already initialized
        """
        if DeltaTable.isDeltaTable(self.spark, self.path):
            return True
        else:
            return False
