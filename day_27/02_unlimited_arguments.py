def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

print(add(23,4,5,6,7))