from pyspark.sql.types import StructField, StructType, StringType, IntegerType

class GoldFactRevenue():

    def __init__(self, config:dict):
        self.name = "Gold_fact_revenue"
        self.schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("Product_id", IntegerType(), True),
            StructField("customer_id", IntegerType(), True),
            StructField("revenue_per_region", IntegerType(), True)
        ])
