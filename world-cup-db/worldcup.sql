-- FCC World Cup Database
CREATE DATABASE worldcup;
\c worldcup
CREATE TABLE teams (team_id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL);
CREATE TABLE games (
  game_id SERIAL PRIMARY KEY, year INT NOT NULL, round VARCHAR(50) NOT NULL,
  winner_id INT REFERENCES teams(team_id), opponent_id INT REFERENCES teams(team_id),
  winner_goals INT, opponent_goals INT
);
