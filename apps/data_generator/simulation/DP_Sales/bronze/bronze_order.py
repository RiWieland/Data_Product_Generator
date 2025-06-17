from simulation.abstract.abstract_table import DataTable
from pyspark.sql.types import StructField, StructType, StringType, IntegerType


class BronzeOrder(DataTable):
    """
    Table on Bronze Layer for Order
    """

    def __init__(self):
        self.name = "bronze_order"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("product_id", StringType(), True),
            StructField("customer_id", IntegerType(), True),
            StructField("quantity_ordered", IntegerType(), True)
    ])

