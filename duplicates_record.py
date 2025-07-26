# Question: Dealing with duplicate records is a common challenge in data processing. How do you efficiently handle  duplicates in your PySpark workflows? 

from pyspark.sql import SparkSession 
from pyspark.sql.functions import col 

# Initialize SparkSession 
spark = SparkSession.builder \ 
.appName("FindDuplicates") \ 
.getOrCreate() 

# Sample data 
data = [("Nikhil", "Laptop", 1500), 
        ("Akash", "Phone", 800), 
        ("Nikhil", "Laptop", 1500), 
        ("Bob", "Tablet", 600), 
        ("Akash", "Phone", 800), 
        ("Dave", "Smartwatch", 300)] 
# Create DataFrame 
df = spark.createDataFrame(data, ["Customer", "Product", "Amount"]) 
# Find duplicates based on Customer and Product columns 
duplicate_rows = df.groupBy("Customer", "Product").count().where(col("count") > 1) 
# Show duplicate rows 
duplicate_rows.show() 

Example Output: 
+--------+--------+-----+ 
|Customer|Product |count| 
+--------+--------+-----+ 
| Akash |  Phone|  2| 
| Nikhil| Laptop|  2| 
+--------+--------+-----+
