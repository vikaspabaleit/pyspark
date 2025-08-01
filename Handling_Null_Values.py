/*
Problem Statament : Handling Null Values
You are provided with a dataset containing customer information. The dataset may have missing values in the customer_id or email columns. Your task is to filter out any rows where either customer_id or email is null.
*/

# Initialize Spark session
from pyspark.sql import SparkSession
#import pandas as pd
spark = SparkSession.builder.appName('Handling Null Values').getOrCreate()

#Copy the starter code or load the file path available in the problem statement 
df = spark.read.format("csv").option("header",True).option("InferSchema",True).load("/datasets/customers_raw.csv")
# Display the final DataFrame using the display() function.

filter_df = df.dropna(subset=['customer_id','email'])
filter_df.show()
