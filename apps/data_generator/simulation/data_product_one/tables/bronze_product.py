from simulation.data_product_one.tables.abstract_table import DataTable
from pyspark.sql.types import StructField, StructType, StringType, IntegerType


class BronzeProduct(DataTable):
    """
    Table on Bronze Layer for Product
    """

    def __init__(self):
        self.name = "bronze_product"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("product", StringType(), True),
            StructField("description", StringType(), True),
            StructField("price", IntegerType(), True)
    ])
