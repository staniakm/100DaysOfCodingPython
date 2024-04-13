travel_log = [
    {"country": "Germany", "visit_count": 2, "city_visited": ["Berlin"]},
    {"country": "France", "visit_count": 4, "city_visited": ["Paris"]}
]


def print_travel_log(travel_log):
    for e in travel_log:
        print(e)


print_travel_log(travel_log)


def add_new_country(country, visits, cities_visited):
    travel_log.append(
        {
            "country": country,
            "visit_count": visits,
            "city_visited": cities_visited
        }
    )


country = input("Country")
visits = int(input("Visit count"))
list_of_cities = eval(input())

add_new_country(country, visits, list_of_cities)

print_travel_log(travel_log)
