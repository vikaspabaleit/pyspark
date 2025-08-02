from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, rank, dense_rank, row_number
from pyspark.sql.window import Window

# Sample data
data = [
    ("Electronics", "Phone", 1000),
    ("Electronics", "Laptop", 1500),
    ("Electronics", "Tablet", 800),
    ("Furniture", "Chair", 300),
    ("Furniture", "Table", 300),
    ("Furniture", "Desk", 600),
]

# Create DataFrame
spark = SparkSession.builder.appName("WindowFunctions").getOrCreate()
df = spark.createDataFrame(data, ["category", "product", "sales"])

# Define window specification
window_spec = Window.partitionBy("category").orderBy("sales")

# Apply window functions
df_transformed = df \
    .withColumn("rank", rank().over(window_spec)) \
    .withColumn("dense_rank", dense_rank().over(window_spec)) \
    .withColumn("row_number", row_number().over(window_spec)) \
    .withColumn("cumulative_sales", sum("sales").over(window_spec)) \
    .withColumn("average_sales", avg("sales").over(window_spec))

df_transformed.show()

category	product	sales
Electronics	Phone	1000
Electronics	Laptop	1500
Electronics	Tablet	800
Furniture	Chair	300
Furniture	Table	300
Furniture	Desk	600

+-----------+-------+-----+----+----------+----------+----------------+-------------+
|   category|product|sales|rank|dense_rank|row_number|cumulative_sales|average_sales|
+-----------+-------+-----+----+----------+----------+----------------+-------------+
|Electronics| Tablet|  800|   1|         1|         1|             800|        800.0|
|Electronics|  Phone| 1000|   2|         2|         2|            1800|        900.0|
|Electronics| Laptop| 1500|   3|         3|         3|            3300|       1100.0|
|  Furniture|  Chair|  300|   1|         1|         1|             600|        300.0|
|  Furniture|  Table|  300|   1|         1|         2|             600|        300.0|
|  Furniture|   Desk|  600|   3|         2|         3|            1200|        400.0|
+-----------+-------+-----+----+----------+----------+----------------+-------------+
