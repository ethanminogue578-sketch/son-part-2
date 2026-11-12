import sqlite3
from bike_data import stations, riders, bikes, hires
 
connection = sqlite3.connect("bike_hire.db")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()
 
# start fresh each time the file runs
cursor.executescript("""
DROP TABLE IF EXISTS hires;
DROP TABLE IF EXISTS bikes;
DROP TABLE IF EXISTS riders;
DROP TABLE IF EXISTS stations;
""")

cursor.execute("""
CREATE TABLE stations (
    station_id INTEGER PRIMARY KEY,
    name       TEXT NOT NULL UNIQUE,
    area       TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE riders (
    rider_id INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    email       TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE bikes (
    bike_id INTEGER PRIMARY KEY,
    bike_type       TEXT NOT NULL UNIQUE,
    station_id       INTEGER NOT NULL
    CHECK (bike_type IN ('standard', 'electric')),
    FOREIGN KEY (station_id)
    REFERENCES stations(station_id)
)
""")

for station in stations:
    cursor.execute(
        "INSERT INTO stations VALUES (?, ?, ?)",
        station,
    )

for rider in riders:
    cursor.execute(
        "INSERT INTO riders VALUES (?, ?, ?)",
        station,
    )

for bike in bikes:
    cursor.execute(
        "INSERT INTO bikes VALUES (?, ?, ?)",
        station,
    )
 
connection.commit()

connection.close()
