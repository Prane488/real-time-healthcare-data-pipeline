from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType

spark = SparkSession.builder.appName("HealthcareStreaming").getOrCreate()

schema = StructType() \
    .add("patient_id", IntegerType()) \
    .add("event_type", StringType()) \
    .add("hospital_id", IntegerType()) \
    .add("timestamp", DoubleType())

stream_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "healthcare-events") \
    .load()

parsed_df = stream_df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

query = parsed_df.writeStream \
    .format("console") \
    .start()

query.awaitTermination()
