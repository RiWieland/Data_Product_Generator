
import os
from utils.utils import get_spark, create_landing_path_data_sink
from config.config_simulation import PATH_DOCKER_SINK, PSYDO_SCHEMA
from simulation.DP_Sales.gold.gold_fact_revenue import GoldFactRevenue
from simulation.DP_Sales.bronze.bronze_customer import BronzeCustomer
from simulation.DP_Sales.bronze.bronze_order import BronzeOrder
from simulation.DP_Sales.bronze.bronze_product import BronzeProduct
from data.dataframe_generator import DataframeGenerator
from data.data_writer import DataWriter


from pyspark.sql.types import StructField, StructField, IntegerType, DoubleType, StringType
import logging
import time

start = time.time()

spark = get_spark()


# parameter



# 1. All required tables are initialized
bronze_customer = BronzeCustomer()
bronze_order = BronzeOrder()
bronze_product = BronzeProduct()
gold_fact_revenue = GoldFactRevenue()

path_bronze_customer = str(PATH_DOCKER_SINK) +str(create_landing_path_data_sink(bronze_order))

# 2. The tables are loaded in accordance to the specification

df_bronze_customer = DataframeGenerator(100000000, bronze_customer.schema).create_df(PSYDO_SCHEMA)
df_bronze_order = DataframeGenerator(100000000, bronze_order.schema).create_df(PSYDO_SCHEMA)
df_bronze_product= DataframeGenerator(100000000, bronze_product.schema).create_df(PSYDO_SCHEMA)
df_gold_fact = DataframeGenerator(100000000, gold_fact_revenue.schema).create_df(PSYDO_SCHEMA)

path_bronze_customer = str(PATH_DOCKER_SINK) +str(create_landing_path_data_sink(bronze_customer))
path_bronze_order = str(PATH_DOCKER_SINK) + str(create_landing_path_data_sink(bronze_order))
path_bronze_product = str(PATH_DOCKER_SINK) + str(create_landing_path_data_sink(bronze_product))
path_gold_fact = str(PATH_DOCKER_SINK) + str(create_landing_path_data_sink(gold_fact_revenue))


DataWriter(df_bronze_customer, path_bronze_customer, spark).write_df_to_delta()
DataWriter(df_bronze_order, path_bronze_order, spark).write_df_to_delta()
DataWriter(df_bronze_product, path_bronze_product, spark).write_df_to_delta()
DataWriter(df_gold_fact, path_gold_fact, spark).write_df_to_delta()


end = time.time()

logging.basicConfig(level=logging.INFO)
