from pyspark.sql.types import StructField, StructType, StringType, IntegerType


class BronzeOrder():

    def __init__(self):
        self.name = "bronze_order"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("product_id", StringType(), True),
            StructField("customer_id", StringType(), True),
            StructField("quantity_ordered", StringType(), True)
    ])

