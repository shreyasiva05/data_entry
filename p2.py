"""
File: p2.py
Author: Shreya Sivakumar

Description:  This program shows the layout of code in a Python file, and greets
the user with the name of the programmer
"""



from dataEntryP2 import fillAttendanceData


# Comment the line above out if your have the load_dictionary function working!!
# Comment the line above out if your have the load_dictionary function working!!
def load_dictionary(infile):
    # param = infile =
    # creating an empty dictionary
    dictionary = {}
    # opening a file and setting it to only read
    project = open(infile, "r")
    line = project.readlines()
    # going through loop to split and save each data to the dictionary
    for i in line:
        i = i.strip()
        Data1 = i.split(", ")
        # Adding the first and last names , first seprating them into two different strings and joining them
        firstname = Data1[0]
        lastname = Data1[1]

        name1 = ", ".join(Data1[0:2])
        # A conditional statement inside a for loop to check whether each element is on the dictionary if not append it.
        if name1 not in dictionary:
            dictionary[name1] = []
        Data2 = ", ".join(Data1[2:4])
        dictionary[name1].append(Data2)
    # return the dictionary
    return dictionary


def display_attendance_data_for_student(name, data):
    # param = name = name of the person to check whether it is in the data
    # param = data = list
    # Conditional statement to check whether the name is in the list if it is true print the name and its values
    if name in data:
        print(name, data[name])
    else:
        # Else no students
        print("No student of this name in the attendance log")


def is_present(name, date, data):
    # param = name = to check whether the name is in the data
    # param = date = date of the person
    # param = data = list

    # conditional statement to find the person is present or not
    if name not in data:
        return False
    else:
        # Looping to check whether the date given is in the data
        for value in data[name]:
            if date in value:
                return True
        return False


def list_all_students_checked_in(date, data):
    # param  = date =
    # param = data = list of keys and values
    total_list = []
    checked_list = []
    for name in data:
        value = data[name]
        for element in value:
            date2 = element.split(", ")[1]
            if date2 == date:
                if name not in checked_list:
                    total_list.append(name)
                    checked_list.append(name)

    return total_list


def list_all_students_checked_in_before(date, timestamp, data):
    # param = date = for comparison
    # param = timestamp = the time to check values from the dictionary
    # param = data = list of keys and values

    # created a new empty list
    checked_list = []
    seconds = int(60)
    seconds_square = 3600
    # Splitting the timestamps into hours and mins and converting altogether into seconds
    timestamp = timestamp.split(":")

    hour = int(timestamp[0])

    mins = int(timestamp[1])
    secs = int(timestamp[2])
    hour_sec = hour * seconds_square
    min_sec = mins * seconds
    # total seconds of the timestamp
    total = hour_sec + min_sec + secs
    # going through the loop for splitting the date and time from the values
    for element in data:

        for index in data[element]:
            list = index.split(", ")
            time1 = list[0]
            date1 = list[1]
            date2 = time1.split(":")

            hour = int(date2[0])
            mins = int(date2[1])
            secs = int(date2[2])
            # Converting the hour, mins to seconds inside the loop
            hour_sec = hour * seconds_square

            min_sec = (mins * seconds_square) / 60

            seconds = hour_sec + min_sec + secs
            # Conditional statement to check whether the date is equal to the date given in the parameter
            if date1 == date:
                # if it is, then checks the total seconds of the timestamp adn the total seconds of each person's time
                if seconds < total and element not in checked_list:
                    # Appends the keys/ name to the empty list
                    checked_list.append(element)

    # prints out the names inside the checked list
    return checked_list


def list_students_attendance_count(data, number, roster):
    """
    :param data:
    :param number: tot
    :param roster:
    :return:
    """
    empty_list = []
    total_list = []

    for element in roster:
        if element in data:
            if len(data[element]) == number:
                total_list.append(element)
        else:
            empty_list.append(element)
    if number == 0:
        return empty_list
    return total_list


def load_roster(rosters):
    # param=  rosters  = importing a list
    # return = list  = a list of rosters file values and keys
    # Created a empty list
    list = []
    project = open(rosters, "r")
    # Looping through the project to add each keys and values
    for each in project:
        i = each.strip()
        list.append(i)
    return list


def get_first_student_to_enter(date, data):
    # param = date  = for comparison
    # param = data = list of keys and values
    # created a new empty list
    checked_list = []

    # going through the loop to and splitting the date from the values
    for element in data:
        for index in data[element]:
            list = index.split(", ")
            date1 = list[1]
            # Conditional statement to check whether they have the same date and adding to the empty list (accroding to the date)
            if date1 == date:
                checked_list.append([element, index])  # Creating a 2d list

    # Slicing the 2d list by the first name, and its time
    name = checked_list[0]
    earliest_name = ", ".join(name[0][0:2])
    earliest_time = name[0][1]
    # looping through the list and slicing accordingly
    for i in checked_list:
        data1 = i[0].split(", ")
        name1 = ", ".join(data1[0:2])
        time = i[1]
        # Comparing the first person's time to each person's time
        if (time < earliest_time):
            # if it is true changing the earliest_time to the other earliest_time
            earliest_time = time
            # Changing the name at the same time
            earliest_name = i[0]
    # Returning the name (prints the name who attended the class first)
    return earliest_name


def print_dictionary(data):
    # param = data = list of keys and values
    # Going through the loop to print the keys and the values
    for i in data:
        print(i, data[i])


def print_list(xlist):
    # param = xList = list of values and keys
    # Going through the loop to pring the element of the list
    for element in xlist:
        print(element)


def print_count(list):
    # param = list = list of keys and values
    # prints out the length of the list
    print("There are", len(list), "for this query ")


#
def connect_to_data_file(filename):
    # will return connection to data file
    infile = ""

    try:
        # infile = open("data.txt", "r")
        # infile = open("dataAllShow1stClass.txt", "r")
        # infile = open("dataAllShow1stAnd2ndClass.txt", "r")
        infile = open(filename, "r")
    except FileNotFoundError:
        print("file was not found, try again")

    return infile  # connection with the file


if __name__ == '__main__':
    #
    # infile = connect_to_data_file("randomData.txt")
    # if(infile):
    #     print("connected to data file...")
    # else:
    #     print("issue with data file... STOP")
    #     exit(1)

    # data = load_dictionary("dataAllShow1stAnd2ndClass.txt")
    data = load_dictionary("att_test_1.txt")
    rosters = load_roster("roster_1.txt")

    # data = fillAttendanceData()
    # data = load_dictionary(infile)
    # ************************
    # OR MANUALLY!!!
    # ************************

    # just making sure the data collected is good
    #print_dictionary(data)
    print_dictionary(data)

    print("********* Looking up Student Attendance Data ***********")
    display_attendance_data_for_student("Richardson, Anna", data)
    display_attendance_data_for_student("Riley, Gloria", data)

    print("********* Looking to see if Student was present on date ***********")
    print(is_present("Garcia, Esperanza", "11/14/2022", data))
    print(is_present("Garcia, Esperanza", "11/14/2022", data))

    # display when students first signed in
    print("**** Students present on this date ****")
    result = list_all_students_checked_in("11/16/2022", data)
    print_list(result)
    print_count(result)

    print("**** Those present on date & before a time assigned ****")
    result = list_all_students_checked_in_before("11/16/2022", "08:51:47", data)
    print_list(result)
    print_count(result)

    print("**** First person to enter on 11/2/2022 ****")
    print(get_first_student_to_enter("11/14/2022", data))
    print("**** First person to enter on 11/3/2022 ****")
    print(get_first_student_to_enter("11/14/2022", data))
    print("**** First person to enter on 11/4/2022 ****")
    print(get_first_student_to_enter("11/16/2022", data))
    print("**** First person to enter on 11/5/2022 ****")
    print(get_first_student_to_enter("11/14/2022", data))
    # list the good students that showed up both days
    print("**** Those who attended BOTH classes ****")
    result = list_students_attendance_count(data, 2, rosters)
    print_list(result)
    print_count(result)

    # list the  students that showed up ONE of the days
    print("**** Those who attended ONE class ****")
    result = (list_students_attendance_count(data, 1, rosters))
    print_list(result)
    print_count(result)

    # list the  students that have not shown up
    print("**** Those who have NOT attended a SINGLE class ****")
    result = (list_students_attendance_count(data, 0, rosters))
    print_list(result)
    print_count(result)

