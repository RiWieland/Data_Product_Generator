from simulation.abstract.abstract_table import DataTable
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

class GoldFactRevenue(DataTable):
    """
    Table on Gold Layer for Revenue
    """

    def __init__(self):
        self.name = "bronze_product"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("Product_id", IntegerType(), True),
            StructField("customer_id", IntegerType(), True),
            StructField("revenue_per_region", IntegerType(), True)
        ])
