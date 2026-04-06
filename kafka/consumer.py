from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'healthcare-events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("Listening to healthcare-events topic...")

for message in consumer:
    event = message.value
    print(f"Received event: {event}")
