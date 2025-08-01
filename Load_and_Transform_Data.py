/*
Problem Statement
You need to process a customer dataset to identify high-value customers. Specifically, you will:

Read data from a CSV file with inferSchema option as true.
Filter customers with a purchase amount more than 100 USD.
Further filter to include only customers aged 30 or above.
Use display(df) to show the final DataFrame.
*/

# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

#Copy the starter code or load the file path available in the problem statement 

df = spark.read.format("csv").option("header", "true").option("inferSchema",True).load("/datasets/customers.csv")

# Filter customers with a purchase amount more than 100 USD
df_filtered = df.filter(df["purchase_amount"] > 100)

# Further filter to include only customers aged 30 or above
df_final = df_filtered.filter(df_filtered["age"] >= 30)

df_selected = df_final.select("customer_id", "name", "purchase_amount")
df_selected.printSchema()

# Show the final DataFrame
df_selected.show()
