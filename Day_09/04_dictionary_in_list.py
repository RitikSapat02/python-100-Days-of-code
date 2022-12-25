travel_log = [
    {
        "country":"France",
        "visites":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visites":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    },
]

def add_new_country(country,visites,cities):
    travel_log.append({
        "country":country,
        "visites":visites,
        "cities":cities
    })

add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)