from pyspark.sql.types import StructField, StructType, StringType, IntegerType


class bronze_time_booking():

    def __init__(self):
        self.name = "bronze_time_booking"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("revenue_per_hour", IntegerType(), True),
            StructField("hour", IntegerType(), True)
  ])
