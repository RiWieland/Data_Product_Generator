from simulation.abstract.abstract_table import DataTable
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

class GoldFactRevenue(DataTable):
    """
    Table on Gold Layer for Revenue
    """

    def __init__(self):
        super().__init__()
        self._name = "gold_fact_revenue"
        self.layer = "gold"
        self.schema = StructType([
            StructField("Product_id", IntegerType(), True),
            StructField("customer_id", IntegerType(), True),
            StructField("revenue_per_region", IntegerType(), True)
        ])

    @property
    def name(self):
        """
        Name of the delta table
        """
        return self._name
