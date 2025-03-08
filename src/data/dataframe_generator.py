"""
Simulates data into a dataframe and writes it using the sink
"""
import string

from pyspark.sql.types import StructField, StructField, IntegerType, DoubleType, StringType
from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, shuffle, round, split, lit, concat, concat_ws, col, substring

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

    def create_df(self):
        """
        the main function to create the df
        loops over the input schema and adds a column for the columns in the schema
        """
        for idx, column in enumerate(self.target_schema):
            if column.dataType == IntegerType():
                self.add_column_int(str(idx))

            if column.dataType == StringType():
                self.add_column_str(str(idx))

            if column.dataType == DoubleType():
                self.add_column_double(str(idx))
        return self.df.drop("init")

    def _initialize_df(self, col_name:str = "init"):
        """
        method for initialize a dataframe with the required row_count
        Adds ID Column 
        """
        df = self.spark.range(1, self.row_count).withColumnRenamed("id", col_name)
        return df

    def add_column_int(self, idx:str):
        """
        add a column of type int to the dataframe
        """
        col_name = "INT_" + idx
        self.df = self.df.withColumn(col_name, round(rand(seed=42)*1000 , 0)) 
        self.df = self.df.withColumn(col_name, self.df[col_name].cast(IntegerType()))

    def add_column_double(self, idx:str):
        """
        add a column of type double to the dataframe
        """
        col_name = "DOUBLE_" + idx

        self.df = self.df.withColumn(col_name, rand(seed=42) *1000 )
        self.df = self.df.withColumn(col_name, self.df[col_name].cast(DoubleType()))

    def add_column_str(self, idx:str):
        """
        adding a random string to a dataframe
        """
        col_name = "STRING_" + idx

        source_char = string.ascii_letters #+ string.digits
        self.df = (self.df.withColumn('source_char', split(lit(source_char), ''))
                    .withColumn(col_name, concat_ws('', col('source_char'))))

        self.df = self.df.withColumn(col_name, substring(self.df[col_name], 0, 10))\
                    .drop("source_char")
