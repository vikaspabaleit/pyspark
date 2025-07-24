# Read the below json data using PySpark ?

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read JSON file").getOrCreate()

json_data = [
  {
    "user_id": "U1",                                               # user
    "name": "Alice",
    "orders": [                                                    # orders
      {
        "order_id": "O1001",
        "amount": 250,
        "items": [                                                 # items
          {"item_id": "I1", "product": "Book", "qty": 2},
          {"item_id": "I2", "product": "Pen", "qty": 5}
        ]
      },
      {
        "order_id": "O1002",
        "amount": 300,
        "items": [
          {"item_id": "I3", "product": "Notebook", "qty": 3}
        ]
      }
    ]
  },
  {
    "user_id": "U2",
    "name": "Bob",
    "orders": [
      {
        "order_id": "O2001",
        "amount": 150,
        "items": [
          {"item_id": "I4", "product": "Eraser", "qty": 1}
        ]
      }
    ]
  }
]
# Flatten the nested JSON
flat_data = []
for user in json_data:
    for order in user["orders"]:
        for item in order["items"]:
            flat_data.append((
                user["user_id"],
                user["name"],
                order["order_id"],
                order["amount"],
                item["item_id"],
                item["product"],
                item["qty"]
            ))

columns = ["user_id", "name", "order_id", "amount", "item_id", "product", "qty"]

df = spark.createDataFrame(flat_data,schema=columns)
df.printSchema()
df.show(truncate=False)

other option 
df = spark.read.option("multiline", "true").json("orders.json")

# Flatten the nested structure
df_flat = df.withColumn("order", explode("orders")) \
            .withColumn("item", explode("order.items")) \
            .select(
                "user_id",
                "name",
                "order.order_id",
                "order.amount",
                "item.item_id",
                "item.product",
                "item.qty"
            )

