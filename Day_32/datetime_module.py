import datetime as dt
now  = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
date = now.date()

print(now,type(now))
print(day,type(day))
print(month,type(month))
print(year,type(year))
print(day_of_week,type(day_of_week))
print(date,type(date))

date_of_birth = dt.datetime(year = 2020,month= 4,day = 19,hour = 4)
print(date_of_birth)