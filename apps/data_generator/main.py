
import os
from utils.utils import get_spark
from config.config_simulation import PATH_DOCKER_SINK
from simulation.data_product_one.tables.bronze_customer import BronzeCustomer
from simulation.data_product_one.tables.bronze_order import BronzeOrder
from data.dataframe_generator import DataframeGenerator
from data.data_writer import DataWriter


from pyspark.sql.types import StructField, StructField, IntegerType, DoubleType, StringType
import logging
import time

start = time.time()

spark = get_spark()



# 1. All required tables are initialized
bronze_customer = BronzeCustomer()
bronze_order = BronzeOrder()




# 2. The tables are loaded in accordance to the specification

df_bronze_customer = DataframeGenerator(100000000, bronze_customer.schema).create_df()
df_bronze_order = DataframeGenerator(100000000, bronze_order.schema).create_df()

path_bronze_customer = str(PATH_DOCKER_SINK) + str(bronze_customer.name)
path_bronze_order = str(PATH_DOCKER_SINK) + str(bronze_order.name)

DataWriter(df_bronze_customer, path_bronze_customer, spark).write_df_to_delta()

DataWriter(df_bronze_order, path_bronze_order, spark).write_df_to_delta()


# data_writer.write_df_to_delta()
end = time.time()

logging.basicConfig(level=logging.INFO)


df = spark.read.format("delta").load(path_to_write)

string = "---------------------------------- count: " + str(df.count())
logging.info(string)
time_passed = end - start
logging.info("-------------time: " + str(time_passed ))

exit()
