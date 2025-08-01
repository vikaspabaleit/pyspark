/* Total Purchases by Customer
Problem Statement
Given a dataset of customer purchases, your task is to group the data by customer and calculate the total purchase amount for each customer. You will need to group by customer_id and sum up the purchase_amount for each individual.
Order the result by customer_id
Example Input
customer_id	name	product_id	purchase_date	purchase_amount
1	John	101	2024-01-01	50
2	Alice	102	2024-01-02	30
1	John	103	2024-01-03	70
3	Bob	104	2024-01-04	60     

Example Output
customer_id	total_purchase
1	120
2	30
3	60

*/
# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

#Copy the starter code or load the file path available in the problem statement 
df = spark.read.format("csv") \
.option("header",True) \
.option("InferSchema",True) \
.load("/datasets/customer_purchases.csv")

group_df = df.groupBy("customer_id") \
    .agg(sum("purchase_amount").alias("total_purchase")) \
    .orderBy("customer_id", ascending=True)


# Display the final DataFrame using the display() function.
group_df.show()



                                                                                                                                                                                                                 
                                                                                                                                                                                                                 
