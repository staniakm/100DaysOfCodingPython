travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
print(travel_log)

travel_log_2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log_2)

travel_log_3 = [
    {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"]},
    {"county": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]}
]

print(travel_log_3)
