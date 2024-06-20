CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    session_name VARCHAR(255),
    timestamp TIMESTAMP
);

CREATE TABLE user_actions (
    id SERIAL PRIMARY KEY,
    action_id VARCHAR(255),
    user_id INTEGER REFERENCES users(id),
    action_type VARCHAR(255),
    action_details JSONB,
    timestamp TIMESTAMP
);

CREATE TABLE system_responses (
    id SERIAL PRIMARY KEY,
    response_id VARCHAR(255),
    action_id VARCHAR(255),
    response_type VARCHAR(255),
    response_details JSONB,
    timestamp TIMESTAMP
);

CREATE TABLE interactions (
    id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES sessions(id),
    user_action_id INTEGER REFERENCES user_actions(id),
    system_response_id INTEGER REFERENCES system_responses(id)
);