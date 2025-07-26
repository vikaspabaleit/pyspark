# How can you use PySpark to clean and standardize product names, especially when they contain similar substrings? 

from pyspark.sql import SparkSession 
from pyspark.sql.functions import regexp_replace 
# Initialize SparkSession 
spark = SparkSession.builder \ 
.appName("Product Name Standardization") \ 
.getOrCreate() 
# Example data 
data = [("Samsung Galaxy S21 Ultra",), 
        ("Samsung Galaxy S21",), 
        ("iPhone 12 Pro Max",), 
        ("iPhone 12",)] 
columns = ["product_name"] 
df = spark.createDataFrame(data, columns) 
# Replace common substrings to standardize product names 
df = df.withColumn("clean_product_name", regexp_replace(df["product_name"], r"Samsung Galaxy", "Samsung")) 
df = df.withColumn("clean_product_name", regexp_replace(df["clean_product_name"], r"iPhone", "Apple iPhone")) 
# Show the updated dataframe 
df.show(truncate=False)
