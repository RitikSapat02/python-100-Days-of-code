l = input("Enter: ").split()
for i in range(len(l)):
    l[i] = int(l[i])

# print(max(l))
highest = 0
for i in l:
    if(i>highest):
        highest = i
print(highest)