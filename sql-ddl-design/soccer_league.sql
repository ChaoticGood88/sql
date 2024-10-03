-- Create Teams Table
CREATE TABLE Teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(100),
    home_stadium VARCHAR(100)
);

-- Create Players Table
CREATE TABLE Players (
    player_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    team_id INT REFERENCES Teams(team_id) ON DELETE SET NULL,
    position VARCHAR(50),
    jersey_number INT,
    age INT,
    height DECIMAL(4, 2),  -- Height in meters
    weight DECIMAL(5, 2)   -- Weight in kg
);

-- Create Referees Table
CREATE TABLE Referees (
    referee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    experience_years INT
);

-- Create Seasons Table
CREATE TABLE Seasons (
    season_id SERIAL PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    season_year VARCHAR(10) UNIQUE NOT NULL  -- Format: '2023-2024'
);

-- Create Games Table
CREATE TABLE Games (
    game_id SERIAL PRIMARY KEY,
    home_team_id INT REFERENCES Teams(team_id) ON DELETE CASCADE,
    away_team_id INT REFERENCES Teams(team_id) ON DELETE CASCADE,
    game_date DATE NOT NULL,
    season_id INT REFERENCES Seasons(season_id) ON DELETE CASCADE,
    home_score INT DEFAULT 0,
    away_score INT DEFAULT 0,
    location VARCHAR(100),
    referee_id INT REFERENCES Referees(referee_id) ON DELETE SET NULL
);

-- Create Goals Table
CREATE TABLE Goals (
    goal_id SERIAL PRIMARY KEY,
    game_id INT REFERENCES Games(game_id) ON DELETE CASCADE,
    player_id INT REFERENCES Players(player_id) ON DELETE CASCADE,
    scored_at_minute INT NOT NULL,
    goal_type VARCHAR(50)  -- Example: 'regular play', 'penalty kick'
);

-- Create Team Standings Table
CREATE TABLE TeamStandings (
    team_id INT REFERENCES Teams(team_id),
    season_id INT REFERENCES Seasons(season_id),
    games_played INT DEFAULT 0,
    wins INT DEFAULT 0,
    losses INT DEFAULT 0,
    draws INT DEFAULT 0,
    points INT DEFAULT 0,
    PRIMARY KEY (team_id, season_id)
);
