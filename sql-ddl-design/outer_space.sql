-- from the terminal run:
-- psql < outer_space.sql

DROP DATABASE IF EXISTS outer_space;

CREATE DATABASE outer_space;

\c outer_space

-- Create Galaxies Table
CREATE TABLE Galaxies (
  galaxy_id SERIAL PRIMARY KEY,
  galaxy_name VARCHAR(255) UNIQUE NOT NULL
);

-- Create Stars Table
CREATE TABLE Stars (
  star_id SERIAL PRIMARY KEY,
  star_name VARCHAR(255) UNIQUE NOT NULL,
  star_type VARCHAR(50),
  galaxy_id INT REFERENCES Galaxies(galaxy_id) ON DELETE CASCADE
);

-- Create Planets Table
CREATE TABLE Planets (
  planet_id SERIAL PRIMARY KEY,
  planet_name VARCHAR(255) UNIQUE NOT NULL,
  orbital_period_in_years FLOAT NOT NULL,
  star_id INT REFERENCES Stars(star_id) ON DELETE CASCADE,
  galaxy_id INT REFERENCES Galaxies(galaxy_id) ON DELETE CASCADE
);

-- Create Moons Table
CREATE TABLE Moons (
  moon_id SERIAL PRIMARY KEY,
  moon_name VARCHAR(255) UNIQUE NOT NULL,
  planet_id INT REFERENCES Planets(planet_id) ON DELETE CASCADE,
  orbital_period_in_days FLOAT,
  diameter_in_km FLOAT
);
