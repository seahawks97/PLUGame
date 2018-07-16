# PLU Game v0.2 by seahawks97 (Steven Tucker)
# Project Started 3 July 2018
# Python v3.6.3
# Last Updated: 16 July 2018

import random
import csv
import os

def main():
     print("Welcome to PLU Game! Follow the commands and answer as correctly as you can!")
     while True:
        first = input("Select an option: (T)est yourself; go to (P)rofiles (not yet implemented); (Q)uit. ").lower()
        if first == "t":
             new_game()
             break
        elif first == "p":
            profile()
            break
        elif first == "q":
            print("Goodbye!")
            exit(1)
        else:
            print("Please type a valid command.")


def new_game():
    # Parsing the dictionary
    mydict = {}
    with open("PLUG_dict.txt", "r") as db:                                   # Special thanks to anonom on StackExchange
        for key, val in csv.reader(db):                                      # for help with this part (user:10067842)
            if len(key) == 1:
                # Difficulty line (if it's 1-long, make it a new key for mydict)
                dif = int(key)
                # Construct the entry for this difficulty, and save its name
                mydict[dif] = {"Difficulty": val}
            else:
                # Simply add it in the dict of the current difficulty
                mydict[dif][key] = val
    #print(mydict)                                                           # Comment out for testing

    # Difficulty selector & slims down the used dictionary
    while True:
        difficulty = input("Select your difficulty: (E)asy; (M)edium; (H)ard; (A)ll; (Q)uit. ").lower()
        if difficulty == "e":
            dif = 1
            del mydict[1]["Difficulty"]
            del mydict[2]
            del mydict[3]
            break
        elif difficulty == "m":
            dif = 2
            del mydict[2]["Difficulty"]
            del mydict[1]
            del mydict[3]
            break
        elif difficulty == "h":
            dif = 3
            del mydict[3]["Difficulty"]
            del mydict[1]
            del mydict[2]
            break
        elif difficulty == "a":
            dif = 4
            for n in mydict:
                del mydict[n]["Difficulty"]
            newdict = {**mydict[1], **mydict[2], **mydict[3]}                      # Puts all into 1 dict
            mydict[4] = newdict
            break
        elif difficulty == "q":
            print("Goodbye!")
            exit(1)
        else:
            print("Please type a valid command.")

    num_items = len(mydict[dif])

    # Gets a valid num of rounds
    while True:
        total_num_rounds = input("How many questions would you like, up to & including " + str(num_items) + "? ")
        try:
            total_num_rounds = int(total_num_rounds)
        except ValueError:
            print("Please type a whole number.")
            continue
        if 1 <= total_num_rounds <= num_items:
            break
        else:
            print("Please type a whole number in the inclusive range 1-" + str(num_items) + ".")

    # Decides which questions to ask: PLUs or names
    # The only difference is to read the keys or values
    while True:
        setting = input("Select one to test yourself on: (P)LUs; (N)ames; (Q)uit. ").lower()
        correct_answered = 0                # +1 if answered correctly

        # Questions asked
        if setting == "p":
            print("You have chosen to be asked the PLU of a given item name.\n")
            confirmation()

            # list_of_keys = list(mydict[dif].keys())             # could be useful later
            rand_plu_list = random.sample(list(mydict[dif].keys()), total_num_rounds)  # gets random list of unique PLUs
            #print(rand_plu_list)                                 # useful for editing (answer key)

            for i in range(total_num_rounds):                  # i is the whole number (inc, exc)
                generated_plu = rand_plu_list[i]                  # random PLU generated from index

                # Parses the value into a readable format
                string_out = ""
                if "_" in mydict[dif][generated_plu]:
                    string_out += mydict[dif][generated_plu].replace("_", " ")
                else:
                    string_out += mydict[dif][generated_plu]

                # Asks the questions & determines if correct
                PLU_input = input("What is the PLU of " + string_out + "? ")
                if PLU_input == generated_plu:
                    correct_answered += 1
                    print("Correct! " + str(correct_answered) + "/" + str(i+1) + " have been answered correctly.\n")
                else:
                    print("Incorrect! " + str(correct_answered) + "/" + str(i+1) + " have been answered correctly. "
                          "The correct PLU is " + generated_plu + ".\n")

            break

        elif setting == "n":
            print("You have chosen to be asked the name of a given PLU.\n")
            confirmation()

            rand_name_list = random.sample(list(mydict[dif].values()), total_num_rounds)  # gets random list of unique names
            #print(rand_name_list)                                  # useful for editing (answer key)

            for i in range(total_num_rounds):                   # i is a whole number (inc, exc)

                generated_name = rand_name_list[i]                # random name generated from index
                for key in mydict[dif].keys():
                    if mydict[dif][key] == generated_name:
                        plu_of_name = key

                # Parse value into readable format, used to compare correct answers
                string_out = ""
                if "_" in generated_name:
                    string_out += generated_name.replace("_", " ")
                else:
                    string_out += generated_name

                # Ask question & determine correctness
                name_input = input("What is the name associated with PLU #" + plu_of_name + "? ").lower()
                if name_input == string_out:
                    correct_answered += 1
                    print("Correct! " + str(correct_answered) + "/" + str(i+1) + " have been answered correctly.\n")
                else:
                    print("Incorrect! " + str(correct_answered) + "/" + str(i+1) + " have been answered correctly. "
                          "The correct name is " + string_out + ".\n")

            break

        elif setting == "q":
            print("Goodbye!")
            exit(1)
        else:
            print("Please type a valid command.")

def profile():
    if not os.path.isfile("profiles.txt"):
        profiles = []
    else:
        with open("profiles.txt", "r") as f:
            profiles = f.read()
            profiles = profiles.split("\n")
            profiles = list(filter(None, profiles))
    return profiles

def confirmation():
    while True:
        ready = input("Are you ready? (Y)es; (Q)uit. ").lower()
        if ready == "y":
            print("")
            break
        elif ready == "q":
            print("Goodbye!")
            exit(1)
        else:
            print("Please type a valid command.")


main()
