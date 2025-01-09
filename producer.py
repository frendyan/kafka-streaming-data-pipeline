from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

def create_fake_user_event():
    """Generate a fake user event"""
    events = ['page_view', 'click', 'purchase']
    pages = ['home', 'product', 'cart', 'checkout']
    
    return {
        'user_id': random.randint(1, 1000),
        'event_type': random.choice(events),
        'page': random.choice(pages),
        'timestamp': datetime.now().isoformat(),
        'value': round(random.random() * 100, 2)
    }

def json_serializer(data):
    """Serialize json data"""
    return json.dumps(data).encode('utf-8')

def create_producer():
    """Create a Kafka producer instance"""
    return KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=json_serializer
    )

def main():
    producer = create_producer()
    topic_name = 'user_events'
    
    try:
        while True:
            event = create_fake_user_event()
            producer.send(topic_name, event)
            print(f"Produced event: {event}")
            time.sleep(1)  # Produce an event every second
            
    except KeyboardInterrupt:
        producer.close()
        print("\nProducer stopped")

if __name__ == "__main__":
    main()