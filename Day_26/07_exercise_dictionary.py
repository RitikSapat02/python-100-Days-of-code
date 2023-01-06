weather_c = {
    "Monday":12,
    "Tuesday":14,  
    "Wednesday":15,
    "Thurday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24,
}

weather_fah = {day:(temp * 9/5)+32 for day,temp in weather_c.items()}
print(weather_fah)