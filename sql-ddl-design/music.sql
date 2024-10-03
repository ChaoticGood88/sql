-- from the terminal run:
-- psql < music.sql

DROP DATABASE IF EXISTS music;

CREATE DATABASE music;

\c music

CREATE TABLE Artists (
  artist_id SERIAL PRIMARY KEY,
  artist_name TEXT UNIQUE NOT NULL
);

CREATE TABLE Producers (
  producer_id SERIAL PRIMARY KEY,
  producer_name TEXT UNIQUE NOT NULL
);

CREATE TABLE Albums (
  album_id SERIAL PRIMARY KEY,
  album_name TEXT UNIQUE NOT NULL,
  release_date DATE
);

CREATE TABLE Songs (
  song_id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  duration_in_seconds INTEGER NOT NULL,
  album_id INT REFERENCES Albums(album_id) ON DELETE CASCADE,
  release_date DATE NOT NULL
);

CREATE TABLE SongArtists (
  song_id INT REFERENCES Songs(song_id) ON DELETE CASCADE,
  artist_id INT REFERENCES Artists(artist_id) ON DELETE CASCADE,
  PRIMARY KEY (song_id, artist_id)
);

CREATE TABLE SongProducers (
  song_id INT REFERENCES Songs(song_id) ON DELETE CASCADE,
  producer_id INT REFERENCES Producers(producer_id) ON DELETE CASCADE,
  PRIMARY KEY (song_id, producer_id)
);
