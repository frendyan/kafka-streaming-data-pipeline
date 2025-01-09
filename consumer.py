from kafka import KafkaConsumer
import json
from datetime import datetime
from database_utils import init_db, user_events
from sqlalchemy.dialects.postgresql import insert

def json_deserializer(data):
    """Deserialize json data"""
    return json.loads(data.decode('utf-8'))

def create_consumer():
    """Create a Kafka consumer instance"""
    return KafkaConsumer(
        'user_events',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=json_deserializer,
        auto_offset_reset='earliest',
        group_id='user_events_group'
    )

def process_event(event, connection):
    """Process and store the consumed event"""
    # Convert timestamp string to datetime
    event_timestamp = datetime.fromisoformat(event['timestamp'])
    
    # Prepare data for insertion
    insert_data = {
        'user_id': event['user_id'],
        'event_type': event['event_type'],
        'page': event['page'],
        'event_timestamp': event_timestamp,
        'value': event['value']
    }
    
    # Insert data into database
    stmt = insert(user_events).values(**insert_data)
    connection.execute(stmt)
    connection.commit()
    
    print(f"""
    Stored event:
    User ID: {event['user_id']}
    Event Type: {event['event_type']}
    Page: {event['page']}
    Timestamp: {event_timestamp}
    Value: {event['value']}
    """)

def main():
    # Initialize database
    engine = init_db()
    consumer = create_consumer()
    
    try:
        with engine.connect() as connection:
            for message in consumer:
                process_event(message.value, connection)
                
    except KeyboardInterrupt:
        consumer.close()
        print("\nConsumer stopped")
    finally:
        engine.dispose()

if __name__ == "__main__":
    main()