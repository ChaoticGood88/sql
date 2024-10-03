-- from the terminal run:
-- psql < air_traffic.sql

DROP DATABASE IF EXISTS air_traffic;

CREATE DATABASE air_traffic;

\c air_traffic

CREATE TABLE Passengers (
  passenger_id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  UNIQUE(first_name, last_name)  -- Ensures no duplicate passenger names
);

CREATE TABLE Airlines (
  airline_id SERIAL PRIMARY KEY,
  airline_name TEXT UNIQUE NOT NULL
);

CREATE TABLE Locations (
  location_id SERIAL PRIMARY KEY,
  city TEXT NOT NULL,
  country TEXT NOT NULL,
  UNIQUE(city, country)  -- Avoids duplicate entries
);

CREATE TABLE Tickets (
  ticket_id SERIAL PRIMARY KEY,
  passenger_id INT REFERENCES Passengers(passenger_id) ON DELETE CASCADE,
  airline_id INT REFERENCES Airlines(airline_id) ON DELETE CASCADE,
  seat TEXT NOT NULL,
  departure TIMESTAMP NOT NULL,
  arrival TIMESTAMP NOT NULL,
  from_location_id INT REFERENCES Locations(location_id) ON DELETE CASCADE,
  to_location_id INT REFERENCES Locations(location_id) ON DELETE CASCADE
);
