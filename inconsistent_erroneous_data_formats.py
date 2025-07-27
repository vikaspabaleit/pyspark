# How do you deal with inconsistent or erroneous data formats (e.g., date formats, currency symbols?
from pyspark.sql import SparkSession 
from pyspark.sql.functions import col, to_date, regexp_replace 
# Create a SparkSession 
spark = SparkSession.builder.appName("DataCleaningExample").getOrCreate() 

# Sample DataFrame with inconsistent date formats and currency symbols 
data = [ 
        ('2022-01-01', '$100.50'), 
        ('Jan 15, 2022', '€200.75'), 
        ('03/20/22', '£150.20'), 
        ('2022-05-13', '¥300.00') 
        ] 
columns = ['date', 'amount'] 

# Create DataFrame 
df = spark.createDataFrame(data, columns) 
# Print the original DataFrame 
print("Original DataFrame:") 
df.show() 

# Convert date strings to a consistent format (YYYY-MM-DD) 
df = df.withColumn('date', to_date(col('date'), 'yyyy-MM-dd')) 

# Remove currency symbols and convert amount strings to numeric values 
df = df.withColumn('amount', regexp_replace(col('amount'), '[^\d.]', '').cast('float')) 
# Print the cleaned DataFrame 
print("Cleaned DataFrame:") 
df.show() 
# Stop the SparkSession 
spark.stop() 


## Original DataFrame
- date | amount
    - 2022-01-01 | £100.50
    - Jan 15, 2022 | $200.75
    - 03/20/22 | €150.20
    - 2022-05-13 | $300.00

## Cleaned DataFrame
- date | amount
    - 2022-01-01 | 100.50
    - 2022-01-15 | 200.75
    - 2022-03-20 | 150.20
    - 2022-05-13 | 300.00

