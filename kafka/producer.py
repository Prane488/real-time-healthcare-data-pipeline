from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    event = {
        "patient_id": random.randint(1000, 9999),
        "event_type": "admission",
        "hospital_id": random.randint(1, 50),
        "timestamp": time.time()
    }
    producer.send('healthcare-events', event)
    time.sleep(2)
