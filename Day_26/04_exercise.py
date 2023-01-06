with open('Day_26/file1.txt') as file1:
    list1 = file1.readlines()
with open('Day_26/file2.txt') as file2:
    list2 = file2.readlines()

result = [int(x) for x in list1 if x in list2]
print(result)