import csv

fields = ["Name", "Age"]

person = []

num_persons = int(input("How many persons you want to enter: "))

for i in range(num_persons):
	name = input("Enter the name: ")

	age = int(input("Enter the age: "))

	if age < 18:
		category = "Child"

	elif 18 <= age <= 60:
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

