from sqlalchemy import create_engine, Table, Column, Integer, String, TIMESTAMP, DECIMAL, MetaData
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'port': 5433,
    'database': 'events_db',
    'user': 'postgres',
    'password': 'postgres'
}

def get_database_url():
    return f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

def create_db_engine():
    """Create SQLAlchemy engine"""
    return create_engine(get_database_url())

# Define the table structure
metadata = MetaData()
user_events = Table(
    'user_events', 
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, nullable=False),
    Column('event_type', String(50), nullable=False),
    Column('page', String(50), nullable=False),
    Column('event_timestamp', TIMESTAMP, nullable=False),
    Column('value', DECIMAL(10,2), nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow)
)

def init_db():
    """Initialize database and create tables"""
    engine = create_db_engine()
    metadata.create_all(engine)
    return engine