/* PySpark and AWS S3: 
 Write PySpark code to save a DataFrame in Parquet format to an S3 bucket. 
 Explain how to overwrite a file stored in S3 using PySpark. * /

from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("write_data_into_s3_bucket")getOrCreate()

data = [ (1,"Durva"),(2,"Aaru") ]
schemas = [ "id","Name"]
df = spark.createDataFrame(data,schemas)
df.printSchema()
df.show()
df.write.mode("overwrite").parquet("s3://bucket-name/folder")


