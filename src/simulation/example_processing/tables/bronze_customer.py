from pyspark.sql.types import StructField, StructType, StringType, IntegerType


class BronzeCustomer():

    def __init__(self):
        self.name = "bronze_customer"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("firstname",StringType(),True),
            StructField("lastname",StringType(),True),
            StructField("address",StringType(),True),
            StructField("country",StringType(),True),
    ])
        
