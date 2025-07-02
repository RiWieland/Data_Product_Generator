
import os
from utils.utils import get_spark
from config.config_simulation import PATH_DOCKER_SINK, PSYDO_SCHEMA
from simulation.DP_Sales.gold.gold_fact_revenue import GoldFactRevenue
from simulation.DP_Sales.bronze.bronze_customer import BronzeCustomer
from simulation.DP_Sales.bronze.bronze_order import BronzeOrder
from simulation.DP_Sales.bronze.bronze_product import BronzeProduct
from data.dataframe_generator import DataframeGenerator
from data.data_writer import DataWriter
from simulation.DP_Sales.loads.gold_fact_revenue_load import load_gold_fact_revenue

from pyspark.sql.types import StructField, StructField, IntegerType, DoubleType, StringType
import logging
import time


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    start = time.time()
    spark = get_spark()

    list_tables = [BronzeCustomer, BronzeOrder, BronzeProduct, GoldFactRevenue]

    for i, class_ in enumerate(list_tables):

        table_class_construct = class_()

        # Bronze tables are created with generated data
        if table_class_construct.layer== "bronze":
        
            df_data = DataframeGenerator(100000000, table_class_construct.schema).create_df(PSYDO_SCHEMA)
            DataWriter(df_data, table_class_construct.path, spark).write_df_to_delta()

        else:
            logging.info("Non-Bronze table called")
            df_gold = load_gold_fact_revenue()

            DataWriter(df_gold, table_class_construct.path, spark).write_df_to_delta()

    # initialze class dynamically:
    #bmodule = __import__(module_name)
    #bclass_ = getattr(module, class_name)
    #binstance = class_()


    end = time.time()

