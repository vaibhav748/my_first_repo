import math

my_dict = {}
roll_no_list = []


def info():
    print(
        "-----------------------------------------------------STUDENT-INFORMATION-PORTAL-------------------------------------------------------------")
    token1 = True
    while token1:
        student_name = input("Enter the name here: ")
        x = student_name.isalpha()
        if x:
            token1 = False
            name = student_name

        else:
            print(f"name can't be {student_name}")


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

    subject_list = ['Hindi', 'English', 'Social Science', 'Maths', 'Sanskrit']
    score_list = []
    count = 4

    while count >= 0:
        try:
            score = float(input(f"Enter the {subject_list[count]} marks here: "))
        except ValueError:
            print("Please enter a integer value.")
            continue
        if 0 <= score <= 100:
            score_list.append(score)
            count -= 1
            continue
        else:
            print("Please enter valid input.")
            continue
    # print(score_list)

    hindi_score = score_list[4]
    eng_score = score_list[3]
    sst_score = score_list[2]
    maths_score = score_list[1]
    sanskrit_score = score_list[0]

    score_list1 = [hindi_score >= 33, eng_score >= 33, sst_score >= 33, maths_score >= 33, sanskrit_score >= 33]

    valid_score_list1 = [0 <= hindi_score <= 100, 0 <= eng_score <= 100, 0 <= sst_score <= 100,
                         0 <= maths_score <= 100, 0 <= sanskrit_score <= 100]

    if all(score_list1):
        result = "PASS"
    else:
        result = "FAIL"

    achieved_score = hindi_score + eng_score + sst_score + maths_score + sanskrit_score
    # print(achieved_score)
    total_score = 500
    percent = (achieved_score / total_score) * 100

    if 90 <= percent <= 100:
        if result == "FAIL":
            grade = 'F'

        else:
            grade = 'A'

    elif 80 <= percent <= 90:
        if result == "FAIL":
            grade = 'F'

        else:
            grade = 'B'

    elif 70 <= percent <= 80:
        if result == "FAIL":
            grade = 'F'

        else:
            grade = 'C'

    elif 60 <= percent <= 70:
        if result == "FAIL":
            grade = 'F'

        else:
            grade = 'D'

    elif 50 <= percent <= 60:
        if result == "FAIL":
            grade = 'F'

        else:
            grade = 'D'

    elif 34 <= percent <= 50:
        if result == "FAIL":
            grade = 'F'

        else:
            grade = 'D'

    else:
        grade = 'F'

    # print(math.trunc(percent))

    dict_info = {"name": name, "roll-no": roll_no, "hindi_score": hindi_score, "eng_score": eng_score,
                 "sst_score": sst_score, "maths_score": maths_score, "sanskrit_score": sanskrit_score,
                 "achieved_score": achieved_score, "percent": percent, "result": result, "grade": grade}
    # print(dict_info)

    my_dict[roll_no] = dict_info
    print(my_dict)


def student_detail():
    info()
    token = 'valid'
    while token == 'valid':
        ask = input("Do you want to enter the student details again: ")
        if ask in ['yes', 'Yes', 'y', 'Y']:
            info()
        elif ask in ['no', 'NO']:
            print("See you again.")
            break
        else:
            token = 'invalid'
            print("See you Again.")


student_detail()


def mark_sheet(roll_no):
    print(
        "----------------------------------------------------------------------------------------------------------------------------------------------")
    print(
        "|                                                         CENTRAL BOARD OF SECONDARY EDUCATION                                               |")
    print(
        "|                                                                     MARKS STATEMENT                                                        |")
    print(
        "|                                                          SECONDARY SCHOOL EXAMINATION, 2021                                                |")
    print(
        "|---------------------------------------------------------------------------------------------------------------------------------------------")
    print("|Name:", my_dict[roll_no]['name'],
          "                                                                                                                               ")
    print("|Roll.No:", my_dict[roll_no]['roll-no'],
          "                                                                                                                         ")
    print(
        "|---------------------------------------------------------------------------------------------------------------------------------------------")
    print(
        "|---------------SUBJECT-LIST -----------------------------MARKS-LIST--------------------------------------------------------------------------")
    print("|               HINDI:                                      ", my_dict[roll_no]['hindi_score'])
    print("|               ENGLISH:                                    ", my_dict[roll_no]['eng_score'])
    print("|               SOCIAL SCIENCE:                             ", my_dict[roll_no]['sst_score'])
    print("|               MATHEMATICS:                                ", my_dict[roll_no]['maths_score'])
    print("|               SANSKRIT:                                   ", my_dict[roll_no]['sanskrit_score'])
    print(
        "|                                                                                                                                            ")
    print(
        f"|--------------MARKS ACHIEVED BY {my_dict[roll_no]['name'].upper()}------------------------------------------------------------------------------------------------------")
    print("|                 ", str(my_dict[roll_no]['achieved_score']))
    print(
        "|                                                                                                                                             ")
    print(
        "|---------------PERCENTAGE--------------------------------------------------------------------------------------------------------------------")
    print("|                ", str("%.2f" % my_dict[roll_no]['percent']), "%")
    print(
        "|                                                                                                                                             ")
    print(
        "|---------------RESULT------------------------------------------------------------------------------------------------------------------------")
    print("|               ", my_dict[roll_no]['result'])
    print("|")
    print(
        "|---------------GRADE-------------------------------------------------------------------------------------------------------------------------")
    print("|                ", my_dict[roll_no]['grade'])


student_roll_no = input("Enter the student roll no. whose marksheet_details do you want to display: ")


def universal():
    # import pdb;pdb.set_trace()
    if student_roll_no in my_dict:
        mark_sheet(student_roll_no)
    else:
        print("Please enter a valid roll. no.")


universal()
