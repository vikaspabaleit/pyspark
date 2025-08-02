from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Sample data
data = [
    (1, "2024-01-01", 100),
    (1, "2024-01-02", 200),
    (1, "2024-01-03", 300),
    (2, "2024-01-01", 50),
    (2, "2024-01-02", 80),
    (2, "2024-01-03", 120),
]

# Create DataFrame
spark = SparkSession.builder.appName("LeadLagTutorial").getOrCreate()
df = spark.createDataFrame(data, ["customer_id", "date", "amount"])

# Define window specification
window_spec = Window.partitionBy("customer_id").orderBy("date")

# Apply lead and lag
df = df.withColumn("next_amount", F.lead("amount", 1).over(window_spec))
df = df.withColumn("previous_amount", F.lag("amount", 1).over(window_spec))
df = df.withColumn("amount_diff", F.col("amount") - F.lag("amount", 1).over(window_spec))

df.show()

+-----------+----------+------+-----------+---------------+-----------+
|customer_id|      date|amount|next_amount|previous_amount|amount_diff|
+-----------+----------+------+-----------+---------------+-----------+
|          1|2024-01-01|   100|        200|           NULL|       NULL|
|          1|2024-01-02|   200|        300|            100|        100|
|          1|2024-01-03|   300|       NULL|            200|        100|
|          2|2024-01-01|    50|         80|           NULL|       NULL|
|          2|2024-01-02|    80|        120|             50|         30|
|          2|2024-01-03|   120|       NULL|             80|         40|
+-----------+----------+------+-----------+---------------+-----------+
