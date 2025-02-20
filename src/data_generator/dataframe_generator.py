"""
Simulates data into a dataframe and writes it using the sink
"""

from pyspark.sql.types import StructField, StructField, IntegerType
from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, shuffle, round

from utils.utils import get_spark

class DataframeGenerator:
    """
    A class to create data artificially
    """

    def __init__(self, row_count:int, schema:StructField, spark:SparkSession = get_spark()):
        self.row_count = row_count
        self.target_schema = schema
        self.spark = spark
        self.df_init = self._initialize_df()

    def _initialize_df(self):
        """
        method for initialize a dataframe with the required row_count
        Adds ID Column 
        """
        df = self.spark.range(1, self.row_count).withColumn('INT', round(rand(seed=42) * 10000, 0))#.cast(IntegerType())
        df = df.withColumn("INT",df.INT.cast(IntegerType()))
        return df

    def add_column_int(self):
        """
        add a column of type int to the dataframe
        """
        df = self.df_init.withColumn('INT', round(rand(seed=42) * 10000, 0))
        df = df.withColumn("INT",df.INT.cast(IntegerType()))
        return df
