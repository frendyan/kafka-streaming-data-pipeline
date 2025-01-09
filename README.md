# Kafka Streaming Pipeline with PostgreSQL

A real-time data streaming pipeline using Apache Kafka and PostgreSQL, designed to showcase data engineering skills. The project simulates user activity events (page views, clicks, purchases), streams them through Kafka, and persists them in a PostgreSQL database for analysis.

## Prerequisites

- Docker and Docker Compose
- Python 3.8+
- pip (Python package manager)

## Technologies Used

- Apache Kafka: Event streaming platform
- PostgreSQL: Data persistence
- SQLAlchemy: SQL toolkit and ORM
- Docker: Containerization
- Python: Programming language

## Installation

1. Clone the repository and locate to project folder:
```bash
cd kafka-streaming-pipeline
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Start the services using Docker Compose:
```bash
docker-compose up -d
```

4. Initialize the database schema:
```bash
docker exec -i postgres psql -U postgres -d events_db < schema.sql
```

## Project Structure

```
kafka-streaming-pipeline/
├── docker-compose.yml     # Docker services configuration
├── producer.py           # Event generator
├── consumer.py          # Event processor with DB integration
├── database_utils.py   # Database connection utilities
├── schema.sql         # PostgreSQL schema definition
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

## Data Flow

1. Producer generates synthetic user events
2. Events are published to Kafka topic 'user_events'
3. Consumer processes events from Kafka
4. Events are stored in PostgreSQL database
5. Data becomes available for analysis

## Usage

1. Start the event producer:
```bash
python producer.py
```

2. Start the event consumer:
```bash
python consumer.py
```