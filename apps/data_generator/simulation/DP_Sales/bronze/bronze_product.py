from simulation.abstract.abstract_table import DataTable
from pyspark.sql.types import StructField, StructType, StringType, IntegerType


class BronzeProduct(DataTable):
    """
    Table on Bronze Layer for Product
    """

    def __init__(self):
        super().__init__()
        self._name = "bronze_product"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("product", StringType(), True),
            StructField("description", StringType(), True),
            StructField("price", IntegerType(), True)
    ])

    @property
    def name(self):
        """
        Name of the delta table
        """
        return self._name
