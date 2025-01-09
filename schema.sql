-- Create events table
CREATE TABLE IF NOT EXISTS user_events (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    page VARCHAR(50) NOT NULL,
    event_timestamp TIMESTAMP NOT NULL,
    value DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for common queries
CREATE INDEX idx_user_id ON user_events(user_id);
CREATE INDEX idx_event_type ON user_events(event_type);
CREATE INDEX idx_event_timestamp ON user_events(event_timestamp);