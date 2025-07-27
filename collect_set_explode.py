
from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_set

# Create Spark session
spark = SparkSession.builder.appName("CollectSetExample").getOrCreate()

# Sample data
data = [("A", "apple"), ("A", "banana"), ("B", "orange"), ("A", "apple")]

df = spark.createDataFrame(data, ["customer", "item"])

# Group by 'customer' and collect unique items
result_df = df.groupBy("customer").agg(collect_set("item").alias("unique_items"))

# Display result
result_df.show()
+--------+------------------+
|customer|      unique_items|
+--------+------------------+
|       A| [banana, apple]  |
|       B| [orange]         |
+--------+------------------+

result_df = result_df.select("customer", explode("unique_items").alias("unique_items"))
result_df.show()
+--------+-------------+
|customer|unique_items|
+--------+-------------+
|       A|      banana|
|       A|       apple|
|       B|      orange|
+--------+-------------+
