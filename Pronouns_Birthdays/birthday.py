# birthday.py
# Author: Kevin Tran
# Course: Data Management w/ Prof. Versoza

import mydate as md

#user I/O
print("How many times should I run the simulation?")

trials = int(input())

print("How many birthdays should I generate per trial?")


times = int(input())

#initialize arrays to appropriate size
birthdates = [None]*(times)
duplicates = [None]*(times)

trial_counter = 0


for repeats in range(trials):

    for tries in range(times):
        birthdates[tries] = md.generate_date(1900, 2018)

    #2
    md.remove_years(birthdates)

    #3. Catch duplicate birthdays and store in this array
    duplicates = md.duplicate(birthdates)

    #4. Print out the duplicate birthdays
    if (len(duplicates) != 0):
        trial_counter += 1
        print("Trial # {0}: {1} dates occur more than once!".format(repeats + 1, len(duplicates)))
        for x in range(len(duplicates)):
            print("({0} {1})".format(md.month_num_to_string(duplicates[x][0]), duplicates[x][1])) #convert dates as numbers to strings

    else:
        print("Trial # {}: No dates are the same.".format(repeats + 1))


#7.

print("""\n Results: \n ===== \nOut of {0} trials,
{1} had dates that were repeated. We can conclude
that you have a {2}% chance of sharing a birthday
with someone if you are in a group of {3} people.""".format(trials, trial_counter, (trial_counter/trials)*100, times))
