"""
Simulates data into a dataframe and writes it using the sink
"""

from pyspark.sql.types import StructField, StructField
from pyspark.sql import SparkSession
from pyspark.sql.functions import rand

from utils.utils import get_spark

class DataframeGenerator:
    """
    A class to create data artificially
    """

    def __init__(self, row_count:int, schema:StructField, spark:SparkSession = get_spark()):
        self.row_count = row_count
        self.target_schema = schema
        self.spark = spark
        self.df = self._initialize_df()

    def _initialize_df(self) -> SparkSession.DataFrame:
        """
        method for initialize a dataframe with the required row_count
        """
        df = self.spark.range(1, 1000, self.row_count)
        return df




