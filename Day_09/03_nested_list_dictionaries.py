capitals = {
    "France":"paris",
    "Germany":"Berlin",
}

# nesting list and dictionary in a dictionary
travel_log = {
    "France" :{"cities_visited":["Paris","Lille","Dijon"],"total_visites":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visites":5},
}

#nesting dictionary in list

travel_log_2 = [
    {
        "country":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visites":12
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visites":5
    },
    
]

