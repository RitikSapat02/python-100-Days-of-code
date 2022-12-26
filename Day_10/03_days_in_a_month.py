def leap(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    return False


def days_in_month(year,month):
    if month>12 or month<1:
        return "Invalid month"
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if(month==2 and leap(year)):
        return 29
    return month_days[month-1]


print(days_in_month(eval(input("Enter Year: ")),eval(input("Enter Month: "))))

3