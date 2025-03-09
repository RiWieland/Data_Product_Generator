import os
import logging
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
from config.config_simulation import PATH_SOURCE

def create_source_dir(path_list: list):
    """
    creates the dir for the source for the simulation
    """
    for path in path_list:
        try:
            os.mkdir(path)
            logging.info(f"Directory '{path}' created successfully.")
        except FileExistsError:
            logging.info(f"Directory '{path}' already exists.")
            continue

def get_spark() -> SparkSession:
    """
    create or get a spark session
    """
    builder = SparkSession.builder.appName("MyApp") \
        .master("local[4]") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")\

    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    return spark
