from simulation.abstract.abstract_table import DataTable
from pyspark.sql.types import StructField, StructType, StringType, IntegerType


class BronzeOrder(DataTable):
    """
    Table on Bronze Layer for Order
    """

    def __init__(self):
        super().__init__()
        self._name = "bronze_order"
        self.layer = "bronze"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("product_id", StringType(), True),
            StructField("customer_id", IntegerType(), True),
            StructField("quantity_ordered", IntegerType(), True)
    ])

    @property
    def name(self):
        """
        Name of the delta table
        """
        return self._name
