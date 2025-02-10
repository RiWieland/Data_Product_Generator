from pyspark.sql.types import StructField, StructType, StringType, IntegerType


class bronze_revenue():

    def __init__(self):
        self.name = "bronze_revenue"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("firstname",StringType(),True),
            StructField("middlename",StringType(),True),
            StructField("lastname",StringType(),True),
            StructField("revenue", IntegerType(), True)
  ])
