def add(n1,n2):
    return n1+n2

def mul(n1,n2):
    return n1*n2

def sub(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1/n2

def calculator(n1,n2,fun):
    return fun(n1,n2)

print(calculator(1,2,add))
print(calculator(1,2,mul))
print(calculator(1,2,sub))
print(calculator(1,2,divide)

)