# mydate.py
# Author: Kevin Tran
# Course: Data Management w/ Prof. Versoza

import random


def is_valid_month_num(n):
#params: n = integer 1-12 representing month
#return: boolean, True if n is between 1-12

    try:
        validParam = int(n)
        if ((validParam >= 1) and (validParam <= 12)):
            return True
        else:
            return False

    except TypeError:
        print("Invalid parameter.")


def month_num_to_string(month_num):
#params: integer 1-12 representing month
#return: month name as string

    if (is_valid_month_num(month_num) == False):
        return None

    else:
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        return months[month_num - 1]



def date_to_string(date_list):
#params: 3 element list [year, month, day]
#return: string version of date_list

    day = str(date_list[2])
    month = month_num_to_string(date_list[1])
    year = date_list[0]

    return ("{0} {1}, {2}".format(month, day, year))


def dates_to_strings(list_of_date_lists):
#params: [[year, month, day], [year, month, day], ...]
#return: [['January 1, 2000'], ...]


     return list(map(date_to_string, list_of_date_lists))


def remove_years(list_of_date_lists):
#params: [[year, month, day], [year, month, day], ...]
#return: [[month, day], [month, day]]
    for date in list_of_date_lists:
        del date[0]

    return list_of_date_lists


def is_leap_year(year):
#params: int year
#return: boolean, True if leap year
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False



def get_num_days_in_month(month_num, year):
#params: int month, int year
#return: int number of days for the month, factoring in leap years

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (is_valid_month_num(month_num)):

        if (is_leap_year(year)):
            february_days = days_in_months[1] + 1
            if (month_num == 2):
                return february_days

            return days_in_months[month_num - 1]

        else:
            return days_in_months[month_num - 1]



def generate_date(start_year, end_year):
#params: int year, int max year
#return: randomized date [year, month num, day]

    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, get_num_days_in_month(month,year))


    if(is_leap_year(year)):
        if(month == 2):
            day = random.randint(1, 29)


    return [year, month, day]


def duplicate(list_birthdays):  #extra function
#params: list of birthdays
#return: list of duplicate birthdays, unique values only
    array = []
    dupes = []
    for i in range(len(list_birthdays)):
        if (list_birthdays[i] not in array):
            array.append(list_birthdays[i])
        elif (list_birthdays[i] not in dupes): #prevent repeats
            dupes.append(list_birthdays[i])


    return(dupes)
