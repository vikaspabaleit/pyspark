# In a PySpark project involving customers and orders data, how would you identify customers who have 
never placed any orders?

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("customer_with_no_orders").getOrCreate()

customers_data = [(1,"John"),
                  (2,"Alice"),
                  (3,"Bob"),
                  (4,"Charlie")]

order_data = [(1,"2024-03-03",1500),
                  (2,"2024-03-03",1500),
                  (3,"2024-03-03",1600),
                  (4,"2024-03-03",1800)]

customers_df = spark.createDataFrame(customers_data, ["CustomerID", "Name"]) 
orders_df = spark.createDataFrame(orders_data, ["CustomerID", "OrderDate", "Amount"])
with_no_orders = customers_df.join(orders_df, 'CustomerID', 'left_anti') 
with_no_orders.show() 

Example Output: 
+----------+-------+ 
|CustomerID|  Name| 
+----------+-------+ 
|      3|   Bob| 
+----------+-------+
                  
                  
