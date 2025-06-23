
from pyspark.sql.functions import lit, col

from simulation.DP_Sales.bronze.bronze_customer import BronzeCustomer
from simulation.DP_Sales.bronze.bronze_product import BronzeProduct
from simulation.DP_Sales.bronze.bronze_order import BronzeOrder
from simulation.DP_Sales.gold.gold_fact_revenue import GoldFactRevenue


def load_gold_fact_revenue():
    '''
    The load for the sivler revenue time
    Input:
    load_conifg: the specification of the load
    '''
    bronze_customer = BronzeCustomer()
    bronze_product = BronzeProduct()
    bronze_order = BronzeOrder()

    df_bronze_customer = bronze_customer.read_data()
    df_bronze_product = bronze_product.read_data()
    df_bronze_order = bronze_order.read_data()

    df_total = df_bronze_order.join(df_bronze_customer, df_bronze_order.customer_id == df_bronze_customer.id, "left")
    df_total = df_total.join(df_bronze_product, df_total.product_id == df_bronze_product.id, "left")
    price = 3
    df_total = df_total.withColumn("revenue_per_region", df_total["quantity_ordered"] * lit(int(price)))
    return df_total["Product_id", "customer_id", "revenue_per_region"]
