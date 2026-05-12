-- FCC Celestial Bodies Database
CREATE DATABASE universe;
\c universe
CREATE TABLE galaxy (galaxy_id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL, age_in_millions_of_years NUMERIC, has_life BOOLEAN, description TEXT);
CREATE TABLE star (star_id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL, galaxy_id INT REFERENCES galaxy(galaxy_id), age_in_millions_of_years NUMERIC, mass_solar NUMERIC, is_spherical BOOLEAN);
CREATE TABLE planet (planet_id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL, star_id INT REFERENCES star(star_id), has_atmosphere BOOLEAN, planet_type VARCHAR(20), distance_from_star NUMERIC);
CREATE TABLE moon (moon_id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL, planet_id INT REFERENCES planet(planet_id), age NUMERIC, is_round BOOLEAN);
CREATE TABLE asteroid (asteroid_id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL, age NUMERIC, has_ice BOOLEAN, mass NUMERIC);
INSERT INTO galaxy (name, age_in_millions_of_years, has_life, description) VALUES
  ('Milky Way', 13600, true, 'Our home galaxy'),
  ('Andromeda', 10000, false, 'Closest spiral galaxy'),
  ('Triangulum', 5000, false, 'Third largest in local group'),
  ('Centaurus A', 12000, false, 'Active radio galaxy'),
  ('Sombrero', 9000, false, 'Edge-on spiral'),
  ('Whirlpool', 4000, false, 'Classic spiral galaxy');
INSERT INTO star (name, galaxy_id, mass_solar, is_spherical) VALUES
  ('Sun', 1, 1.0, true),
  ('Proxima Centauri', 1, 0.12, true),
  ('Sirius A', 1, 2.06, true),
  ('Alpha Centauri B', 1, 0.91, true),
  ('Vega', 1, 2.1, true),
  ('Betelgeuse', 1, 11.6, true);
INSERT INTO planet (name, star_id, has_atmosphere, planet_type) VALUES
  ('Earth', 1, true, 'terrestrial'),
  ('Mars', 1, true, 'terrestrial'),
  ('Venus', 1, true, 'terrestrial'),
  ('Jupiter', 1, true, 'gas giant'),
  ('Saturn', 1, true, 'gas giant'),
  ('Uranus', 1, true, 'ice giant'),
  ('Neptune', 1, true, 'ice giant'),
  ('Mercury', 1, false, 'terrestrial'),
  ('Pluto', 1, false, 'dwarf'),
  ('Proxima b', 2, true, 'terrestrial'),
  ('Sirius A b', 3, true, 'gas giant'),
  ('Vega c', 5, true, 'gas giant');
INSERT INTO moon (name, planet_id) VALUES
  ('Moon', 1), ('Phobos', 2), ('Deimos', 2),
  ('Io', 4), ('Europa', 4), ('Ganymede', 4), ('Callisto', 4),
  ('Titan', 5), ('Mimas', 5), ('Enceladus', 5), ('Tethys', 5), ('Dione', 5), ('Rhea', 5), ('Iapetus', 5),
  ('Miranda', 6), ('Ariel', 6), ('Umbriel', 6), ('Titania', 6), ('Oberon', 6),
  ('Triton', 7);
