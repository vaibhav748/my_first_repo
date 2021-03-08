# import math
#
# name = input("Enter the name:")
# roll_no = input("Enter the roll no.:")
# print(
#     "----------------------------------------------------Enter Student Marks Out Of 100-----------------------------------------------------------")
# hindi_score = int(input("Enter Hindi Score: "))
# eng_score = int(input("Enter English Score: "))
# sst_score = int(input("Enter Social Science Score: "))
# maths_score = int(input("Enter Mathematics Score: "))
# sanskrit_score = int(input("Enter Sanskrit Score: "))
#
# achieved_score = hindi_score + eng_score + sst_score + maths_score + sanskrit_score
# print(achieved_score)
# total_score = 500
# percent = (achieved_score / total_score) * 100
# print(math.trunc(percent))
#
# score_list = [hindi_score >= 33, eng_score >= 33, sst_score >= 33, maths_score >= 33, sanskrit_score >= 33]
#
# valid_score_list = [0 <= hindi_score <= 100, 0 <= eng_score <= 100, 0 <= sst_score <= 100, 0 <= maths_score <= 100, 0 <= sanskrit_score <= 100]
#
# if all(score_list):
#     result = "PASS"
# else:
#     result = "FAIL"
#
#
# def student_grade():
#     if 90 <= percent <= 100:
#         if result == "FAIL":
#             grade = 'F'
#             return grade
#         else:
#             grade = 'A'
#             return grade
#     elif 80 <= percent <= 90:
#         if result == "FAIL":
#             grade = 'F'
#             return grade
#         else:
#             grade = 'B'
#             return grade
#     elif 70 <= percent <= 80:
#         if result == "FAIL":
#             grade = 'F'
#             return grade
#         else:
#             grade = 'C'
#             return grade
#     elif 60 <= percent <= 70:
#         if result == "FAIL":
#             grade = 'F'
#             return grade
#         else:
#             grade = 'D'
#             return grade
#     elif 50 <= percent <= 60:
#         if result == "FAIL":
#             grade = 'F'
#             return grade
#         else:
#             grade = 'D'
#             return grade
#     elif 34 <= percent <= 50:
#         if result == "FAIL":
#             grade = 'F'
#             return grade
#         else:
#             grade = 'D'
#             return grade
#     else:
#         grade = 'F'
#         return grade
#
#
#
# def mark_sheet():
#     print(
#         "----------------------------------------------------------------------------------------------------------------------------------------------")
#     print(
#         "|                                                         CENTRAL BOARD OF SECONDARY EDUCATION                                               |")
#     print(
#         "|                                                                     MARKS STATEMENT                                                        |")
#     print(
#         "|                                                          SECONDARY SCHOOL EXAMINATION, 2021                                                |")
#     print(
#         "|---------------------------------------------------------------------------------------------------------------------------------------------")
#     print("|Name:", name,
#           "                                                                                                                               ")
#     print("|Roll.No:", roll_no,
#           "                                                                                                                         ")
#     print(
#         "|---------------------------------------------------------------------------------------------------------------------------------------------")
#     print(
#         "|---------------SUBJECT-LIST -----------------------------MARKS-LIST--------------------------------------------------------------------------")
#     print("|               HINDI:                                      ", hindi_score)
#     print("|               ENGLISH:                                    ", eng_score)
#     print("|               SOCIAL SCIENCE:                             ", sst_score)
#     print("|               MATHEMATICS:                                ", maths_score)
#     print("|               SANSKRIT:                                   ", sanskrit_score)
#     print(
#         "|                                                                                                                                            ")
#     print(
#         f"|--------------MARKS ACHIEVED BY {name.upper()}---------------------------------------------------------------------------------------------------")
#     print("|                 ", str(achieved_score))
#     print(
#         "|                                                                                                                                             ")
#     print(
#         "|---------------PERCENTAGE--------------------------------------------------------------------------------------------------------------------")
#     print("|                ", str("%.2f" % (percent)), "%")
#     print(
#         "|                                                                                                                                             ")
#     print(
#         "|---------------RESULT------------------------------------------------------------------------------------------------------------------------")
#     print("|               ", result)
#     print("|")
#     print(
#         "|---------------GRADE-------------------------------------------------------------------------------------------------------------------------")
#     print("|                ", student_grade())
#
#
# if all(valid_score_list):
#     mark_sheet()
# else:
#     print("You are giving some invalid output.")
# token = True
# while token:
#     student_name = input("Enter the name here: ")
#     x = student_name.isalpha()
#     if x:
#         token = False
#         name = student_name
#         print(name)
#     else:
#         print(f"name can't be {student_name}")

# roll_no_list = []
# student_roll_no = int(input("Enter the roll.no here: "))
# token = True
# while token:
#     if student_roll_no in roll_no_list:
#         print(f"The roll. no {student_roll_no} is occupied by another student.")
#     else:
#         token = False
#         roll_no_list.append(student_roll_no)
#         roll_no = student_roll_no
#         print(roll_no)
#
#     print(roll_no_list)


roll_no_list = []
token2 = True
while token2:
    student1_roll_no = input("Enter the roll.no here: ")
    x = student1_roll_no.isnumeric()
    if x:
        if student1_roll_no in roll_no_list:
            print(f"The roll. no {student1_roll_no} is occupied by another student. please enter a valid roll. no")
        else:
            token2 = False
            roll_no_list.append(student1_roll_no)
            roll_no = student1_roll_no
    else:
        print("Please enter valid roll.no.")









