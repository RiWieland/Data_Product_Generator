
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

from utils.utils import get_spark
from simulation.abstract.abstract_table import DataTable


class BronzeCustomer(DataTable):
    """
    Table on Bronze Layer for Customer
    """
    def __init__(self):
        super().__init__()
        self._name = "bronze_customer"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("firstname",StringType(),True),
            StructField("lastname",StringType(),True),
            StructField("address",StringType(),True),
            StructField("country",StringType(),True),
    ])
        self.partition_by = StructField("id", IntegerType(), True)

    @property
    def name(self):
        """
        Name of the delta table
        """
        return self._name
