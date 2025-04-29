from simulation.data_product_one.tables.abstract_table import DataTable
from pyspark.sql.types import StructField, StructType, StringType, IntegerType


class BronzeCustomer(DataTable):
    """
    Table on Bronze Layer for Customer
    """
    def __init__(self):
        self.name = "bronze_customer"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("firstname",StringType(),True),
            StructField("lastname",StringType(),True),
            StructField("address",StringType(),True),
            StructField("country",StringType(),True),
    ])
        self.partition_by = StructField("id", IntegerType(), True)
