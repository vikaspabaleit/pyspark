# Can you share any experience or example of a challenging data cleaning task you've encountered in Spark, and  how you addressed it?

from pyspark.sql import SparkSession 
from pyspark.sql.functions import when, to_date 
# Create a SparkSession 
spark = SparkSession.builder.appName("DateCleaningExample").getOrCreate() 

# Sample DataFrame with inconsistent date formats 
data = [ 
        ('2022-01-01',), 
        ('Jan 15, 2022',), 
        ('03/20/22',), 
        ('2022-05-13',) 
        ] 
columns = ['date'] 
# Create DataFrame 
df = spark.createDataFrame(data, columns) 
# Print the original DataFrame 
print("Original DataFrame:") 
df.show() 
# Standardize date formats to 'yyyy-MM-dd' 
df = df.withColumn( 'date', when(df['date'].rlike(r'^\d{4}-\d{2}-\d{2}$'), df['date']) # yyyy-MM-dd 
                           .when(df['date'].rlike(r'^\w{3} \d{1,2}, \d{4}$'), to_date(df['date'], 'MMM dd, yyyy')) # MMM dd, yyyy 
                           .when(df['date'].rlike(r'^\d{2}/\d{2}/\d{2}$'), to_date(df['date'], 'MM/dd/yy')) # MM/dd/yy 
                           .otherwise(None) 
                        ) 
# Print the cleaned DataFrame 
print("Cleaned DataFrame:") 
df.show() 
# Stop the SparkSession 
spark.stop() 


Original DataFrame:
| date |
| --- |
| 2022-01-01 |
| Jan 15, 2022 |
| 03/20/22 |
| 2022-05-13 |

Cleaned DataFrame:
| date |
| --- |
| 2022-01-01 |
| 2022-01-15 |
| 2022-03-20 |
| 2022-05-13 |

