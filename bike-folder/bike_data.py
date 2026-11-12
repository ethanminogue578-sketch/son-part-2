# bike_data.py: sample data for Harbourside Bike Hire (a fictional business)
# Use it in your own file with:
#     from bike_data import stations, riders, bikes, hires

# (station_id, name, area)
stations = [
    (1, "Quayside", "Centre"),
    (2, "Station Road", "East"),
    (3, "Park Gate", "North"),
    (4, "Mill Lane", "East"),
]

# (rider_id, name, email)
riders = [
    (1, "Aisha Khan", "aisha@example.com"),
    (2, "Ben Carter", "ben@example.com"),
    (3, "Chloe Evans", "chloe@example.com"),
    (4, "Dan Wright", "dan@example.com"),
    (5, "Ella Brooks", "ella@example.com"),
    (6, "Femi Adeyemi", "femi@example.com"),
]

# (bike_id, bike_type, station_id)
bikes = [
    (1, "standard", 1), (2, "standard", 1), (3, "electric", 1),
    (4, "standard", 2), (5, "electric", 2),
    (6, "standard", 3), (7, "electric", 3),
    (8, "electric", 4),
]

# (hire_id, rider_id, bike_id, hire_date, hours)
hires = [
    (1, 1, 3, "2026-11-02", 2),
    (2, 2, 1, "2026-11-02", 1),
    (3, 1, 5, "2026-11-04", 3),
    (4, 3, 7, "2026-11-05", 6),
    (5, 4, 2, "2026-11-07", 1),
    (6, 5, 8, "2026-11-07", 4),
    (7, 1, 3, "2026-11-08", 2),
    (8, 6, 4, "2026-11-08", 5),
    (9, 2, 6, "2026-11-09", 1),
    (10, 3, 5, "2026-11-10", 8),
    (11, 1, 7, "2026-11-11", 2),
    (12, 4, 1, "2026-11-11", 3),
]
