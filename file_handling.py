# import csv

# fields = ["Name", "Child", "Adult", "Sr.Citizen"]

# data = [['John', 12, 23, 62],
#         ['Mike', 10, 30, 78],
#         ['Tom', 6, 29, 80],
#         ['Henry', 5, 20, 97]]

# filename = "my_file.csv"

# with open(filename, 'w') as csvfile:
# 	csvwriter = csv.writer(csvfile)

# 	csvwriter.writerow(fields)
# 	csvwriter.writerows(data)

# f = open('my_file.csv', 'r')
# print(f.read())

# # Code for removing a file. 
# # import os
# # if os.path.exists("my_file.csv"):
# #   os.remove("my_file.csv")
# # else:
# #   print("The file does not exist")

# # f = open("my_file.csv", "r")
# # print(f.read())

# # f = open("my_file.csv", "r")
# # print(f.read(2))

# # w = open("my_file.csv", "r")
# # print(w.readline())
# # print(w.readline())

# # with open("my_file.csv", 'r') as file:
# #     csv_file = csv.DictReader(file)
# #     for row in csv_file:
# #         print(dict(row))

# # age = int(input("Enter the age here: "))

# # if age < 18:
# # 	pass
# # elif age >= 18:
# # 	pass
# # else:
# # 	pass

# x = open("my_file.csv",'r')
# y = open("y_only.csv",'w',newline='')

# for i in x:
# 	age = input("Enter the age here: ")
# 	print(i)
#     if i[0]:
#         y.write(i)

# yn.close()
# y.close()

import csv

fields = ["Name", "Age"]

person = []

num_persons = int(input("How many persons you want to enter: "))

for i in range(num_persons):
	name = input("Enter the name: ")

	age = int(input("Enter the age: "))

	if age < 18:
		category = "Child"

	elif age >= 18 and age <= 60:
		category = "Adult"

	else:
		category = "Sr.citizen"
	person.append([name, category])

# print(person)

filename = "my_file.csv"

with open(filename, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)

	csvwriter.writerow(fields)
	csvwriter.writerows(person)

f = open('my_file.csv', 'r')
print(f.read())
f.close()

# >>> import csv
# >>> persons=[('Lata',22,45),('Anil',21,56),('John',20,60)]
# >>> csvfile=open('persons.csv','w', newline='')
# >>> obj=csv.writer(csvfile)
# >>> for person in persons:
# >>> obj.writerow(person)
# >>> csvfile.close()