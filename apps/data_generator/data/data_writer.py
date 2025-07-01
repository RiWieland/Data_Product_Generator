"""
write the dataframe in delta files in the sink
"""
from utils.utils import get_spark
from delta.tables import DeltaTable
from pyspark.sql import SparkSession, DataFrame


class DataWriter:
    """
    A class to write data to a file
    """
    def __init__(self, df:DataFrame, path:str, partition_by:str, spark:SparkSession = get_spark()):
        self.df = df
        self.path = path
        self.partition_by = partition_by
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

    def init_delta(self) -> bool:
        """
        write a empty dataframe with the schem
        """
        empty_df = self.spark.createDataFrame([], self.df.schema) # spark is the Spark Session
        empty_df.write.format("delta").mode("overwrite").save(str(self.path))
        return True

    def write_df_to_delta(self):
        """
        method to write spark dataframe to delta
        """
        if not self._is_delta_initialized:
            self.init_delta()
        self.df.write.format("delta").mode("append").save(self.path)
