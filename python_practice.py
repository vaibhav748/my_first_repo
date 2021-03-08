# my_dict = {"name": "vaibhav",
#            "surname": "mathur",
#            "age": 21}

# print(my_dict)

# print(my_dict["age"])

# print(len(my_dict))

# print(type(my_dict))

# # x = my_dict.get("name")
# # print(x)

# y = my_dict.keys()
# print(y)

# my_dict["company"] = "ThoughtWin IT Solutions Pvt. Ltd"

# print(my_dict)

# z = my_dict.keys()
# print(z)

# x = my_dict.values()
# print(x)

# if "name" in my_dict:
# 	print("name exists in my_dict.")

# for i in my_dict:
# 	print(i)

# for x in my_dict.keys():
# 	print(x)

# for x in my_dict.values():
# 	print(x)

# for x, y in my_dict.items():
# 	print(x, y)

# my_dict1= {"name": "vaibhav",
#            "surname": "mathur",
#            "age": 21}

# # Copying the Dictionaries
# my_dict2 = my_dict1.copy()
# print(my_dict2)

# my_dict3 = dict(my_dict1)
# print(my_dict3)

# thislist = [10, 20, 30, 40, 50, 60]
# print(thislist)

# thislist.append(70)

# x = thislist.pop(0)
# print(x)

# print(thislist)

# print(len(thislist))

# print(type(thislist))

# my_set = {1, 2, 3, 4, 5, 6, 1}
# print(my_set)

# my_set.add(20)
# print(my_set)

# my_set.remove(2) # we can also use discard() method.
# print(my_set)

# my_set.pop()
# print(my_set) # Removes last item.

# my_list = ["john", "johnson", "micky"]

# max_len = 0

# for word in my_list:
# 	if len(word) > max_len:
# 		max_len = len(word)
# 		longest_word = word
		

# print("Longest word is: " + longest_word)

# x = lambda a: a**2
# print('Answer : ' + str(x(2)))

# y = lambda a, b: a**b
# print(y(2, 3))

# print("{}, a solution oriented company.".format("ThoughtWin"))

# z = lambda a, b, c: (a + b + c)
# print("Answer is: {}".format(z(1, 2, 3)))

# name = "vaibhav"
# age = 21

# def my_func():
# 	print("my Name is {} and i am {} years old.".format(name, age))

# my_func()

# x = 10

# while x > 3:
# 	print(x)
# 	x -= 1

# class parent:
# 	def __init__(self, first_name, last_name):
# 		self.first_name = first_name
# 		self.last_name = last_name

# 	def full_name(self):
# 		print("My full name is: " + self.first_name +" "+ self.last_name)

# x = parent("vaibhav", "mathur")
# print(x.first_name)

# x.full_name()

# class child(parent):
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def intro(self):
# 		print("My name is {} and i am {} years old.".format(self.name, self.age))

# 	def full_name(self):
# 		print("My full name is: " + self.name)

# y = child("John", 24)
# y.intro()

# y.full_name()

# class grandchild(child, parent):
# 	def __init__(self, first_name, last_name, age):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.age = age

# 	def introduction(self):
# 		print("Hello my name is {} and i am the grandchild of {}.".format(self.first_name, x.first_name))

# z = grandchild("John", "Miller", 68)
# z.introduction()

# name = "johnson"

# my_iter = iter(name)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))


# age = 12

# try:
# 	# age / 0
# 	name = vaibhav
# except ZeroDivisionError:
# 	print("There is a ZeroDivisionError in this code.")
# except NameError:
# 	("Some other error in this code.")
# finally:
# 	print("it's all over.")

# # List Comprehensions.

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_list = []

# for item in my_list:
# 	if item % 2 == 0:
# 		new_list.append(item)

# print("New List is: ", new_list)

# my_list1 = [1, 2, 3, 6, 78, 34, 21, 45, 98, 50, 98]

# even_list = [x for x in my_list1 if x % 2 == 0]

# odd_list = [x for x in my_list1 if x % 2 != 0]

# print("Even List is: ", even_list)

# print("Odd List is:", odd_list)

# my_list2 = []

# for i in range(1, 11):
# 	my_list2.append(i ** 2)

# print("My_list2 is:", my_list2)

# sqr_list = [x**2 for x in range(1, 11)]

# print("Square_list is:", sqr_list)

# # Dictionary Comprehensions

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_dict = {}

# for num in my_list:
# 	if num % 2 != 0:
# 		my_dict[num] = num ** 3

# print("Dictionary is:", my_dict)

# my_dict1 = {key: key ** 2 for key in my_list if key % 2 != 0}

# print("My_dict1 is:", my_dict1)

# state = {"MP", "MH", "RAJ", "GUJ"}

# capital = {"BHOPAL", "MUMBAI", "JAIPUR", "AHMEDABAD"}

# out_dict = {}

# for key, value in zip(state, capital):
# 	out_dict[key] = value

# print("Answer is: ", out_dict)

# out_dict1 = {key: values for key, values in zip(state, capital)}

# print(out_dict1)

# # Set Comprehensions

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# my_set = {x for x in my_list if x % 2 != 0}

# print(my_set)

# # Tuples

# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# print(my_tuple[-1])

# print(my_tuple[1: 7])

# Map Function

# my_list = [1, 2, 3, 4, 5, 6]

# def sqr(n):
# 	return n * n

# square = list(map(sqr, my_list))

# print(square)

# my_list2 = [10, 20, 30, 40]

# new_list = list(map(lambda x: x // 2, my_list2))

# print(new_list)

# my_list3 = ["trainee", "developer", "team lead"]

# caps = list(map(lambda x: x.upper(), my_list3))

# print(caps)

# # Filter Function

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_list = list(filter(lambda x: x % 2 == 0, my_list))

# odd_list = list(filter(lambda x: x % 2 != 0, my_list))

# print(even_list)

# print(odd_list)

# # Reduce Function

# from functools import reduce

# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# answer = reduce(lambda x, y: x + y, my_tuple)

# print("Answer is: ", answer)

# # Zip Function

# name = ["Jack", "John", "Mike"]

# roll_no = [1, 2, 3]

# marks = [10, 23, 44]

# info = zip(name, roll_no, marks)

# print(list(info))

# information = zip(name, marks)

# print(dict(information))

# Datetime 

# import datetime

# x = datetime.datetime.now()

# print("Today's datetime is: " + str(x))

# y = datetime.datetime.now()

# print(y.year)

# print(y.strftime("%A"))

# print(y.strftime("%a"))

# print(y.strftime("%B"))

# print(y.strftime("%b"))

# z = datetime.datetime(2020, 7, 12)

# print(z)

# w = datetime.datetime(1996, 7, 13)

# print(w.strftime("%B"))

# # Generator Functions

# def my_generator():
# 	yield 1
# 	yield 2
# 	yield 3

# for value in my_generator():
# 	print(value)

# def my_generator1():
# 	yield 1
# 	yield 2
# 	yield 3

# x = my_generator1()

# print(x.next())
# print(x.next())
# print(x.next())


# name = input("Enter here:")
# print("Name:" + name)

# for i in range(10):
# 	name = input("Enter the name: ")
# 	age = int(input("Enter the age: "))
# 	if age < 18:
# 		category = "Child"
# 	elif age >= 18:
# 	    category = "Adult"
#     else:
# 	    category = "Sr.citizen"
# 	person.append([name, category])
# print(person)

person = []

for i in range(10):
	name = input("Enter the name: ")

	age = int(input("Enter the age: "))

	if age < 18:
		category = "Child"
	elif age >= 18:
		category = "Adult"
	else:
		category: "Sr.citizen"
	person.append([name, category])

print(person)