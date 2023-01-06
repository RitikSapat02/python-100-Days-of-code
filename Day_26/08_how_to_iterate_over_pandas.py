student_dict = {
    "student" : ["Angela","James","Lily"],
    "score":[56,76,98],
}
#loop through dictionary
 
# for key,values in student_dict.items():
#     print(values)


import pandas
student_dataframe = pandas.DataFrame(student_dict)


#loop through pandas datafram

for (index,row) in student_dataframe.iterrows():
    if row.student == "Angela":
        print(row.score)