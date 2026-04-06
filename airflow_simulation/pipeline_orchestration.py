def extract():
    print("Extracting data from Kafka")

def transform():
    print("Transforming data in Databricks")

def load():
    print("Loading curated data to analytics layer")

def run_pipeline():
    extract()
    transform()
    load()

if __name__ == "__main__":
    run_pipeline()
