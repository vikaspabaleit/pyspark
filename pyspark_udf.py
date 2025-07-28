#Explain PySpark UDF with the help of an example.
# A User Defined Function (UDF) in PySpark is a way to extend the built-in functionality of Spark by writing custom functions in Python and applying them to DataFrame columns.

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# 1. Spark session
spark = SparkSession.builder.appName("UDF Example").getOrCreate()

# 2. Sample data
data = [("alice"), ("bob"), ("charlie")]
schema = ["name"]
df = spark.createDataFrame(data, schema)

# 3. Normal Python function
def to_upper(name):
    return name.upper()

# 4. Register UDF
to_upper_udf = udf(to_upper, StringType())

# 5. Use UDF
df_with_upper = df.withColumn("name_upper", to_upper_udf("name"))

df_with_upper.show()

+-------+-----------+
|  name | name_upper|
+-------+-----------+
| alice |    ALICE  |
|  bob  |     BOB   |
|charlie|  CHARLIE  |
+-------+-----------+
