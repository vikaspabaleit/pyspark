/*Important:
map() is an RDD transformation, used to apply a function to each element of the RDD.

In DataFrames, similar functionality can be achieved using:
withColumn()
selectExpr()
UDFs or built-in functions */

from pyspark.sql import SpartSession

spark = SparkSession.builder.appName("map function ").getOrCreate()

# Create RDD
data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
rdd = spark.sparkContext.parallelize(data)

# Apply map() to transform each record
mapped_rdd = rdd.map(lambda x: (x[0], x[1] * 10))

# Collect results
print(mapped_rdd.collect())

Output:
[('Alice', 10), ('Bob', 20), ('Charlie', 30)]

# Equivalent in DataFrame (using withColumn)

from pyspark.sql.functions import col

# Convert RDD to DataFrame
df = rdd.toDF(["name", "value"])

# Multiply 'value' column by 10
df_new = df.withColumn("value", col("value") * 10)

df_new.show()

+-------+-----+
|  name |value|
+-------+-----+
| Alice |  10 |
|  Bob  |  20 |
|Charlie|  30 |
+-------+-----+

