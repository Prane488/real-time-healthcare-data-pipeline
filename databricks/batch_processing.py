from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HealthcareBatchProcessing").getOrCreate()

df = spark.read.json("datasets/sample_events.json")

aggregated_df = df.groupBy("hospital_id").count()

aggregated_df.show()
