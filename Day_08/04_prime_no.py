def prime_checker(num):
    if(num==2):
        return "a prime number"
    
    for i in range(2,num):
        if(num%i==0):
            return "not a prime number"
    
    return "a prime number"

a = int(input("Enter a number: "))
print(f"{a} is {prime_checker(num = a)}")
