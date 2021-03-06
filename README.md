# PLUGame v0.2
## How to Play
1. Download the files *PLUG_dict.txt* and *PLUGame.py*
2. Open command prompt
3. Change directories to your downloads (something like *"cd C:\User\path\to\downloads"*)
4. Type *"python PLUGame.py"*
## Introduction
This is a text-based game to help one remember the PLUs of produce items at Food Lion, where I work. PLUG randomizes the content and tracks how well one has done in inputting the correct answer. I made this game for fun but might pass it off to my managers at Food Lion (I'm a cashier) to see if it would be of any use.
## How it works
~~*I don't feel like working on this right now, I will be back*~~
Ok, I'm back.
### Testing
PLUGame starts with a main menu-type line, where you may select to test yourself, go to the profiles menu, or quit. Quit just exits the program, and profiles has not been implemented yet (see TODO.md).
#### Dictionary
In test mode, the external CSV file, PLUG_dict.txt, is parsed into readable terms with easy output for later use. *Special thanks to [user "anonom" on StackExchange](https://stackoverflow.com/users/10067842/anonom) for helping with this part.* This allows me to catch if the key (first value) of the dictionary is 1-length long, and assigns that as the difficulty level. This works because the first line must be the difficulty line, and the rest of the lines are appended to a sub-dictionary that must have a key (the difficulty) before it. IMO, this is beautiful code that allows for a ton of flexibility and easy-access parts of code that will be used later. (/help from anonom).
#### Trimming & Difficulty Selector
Difficulty (Easy/Medium/Hard/All) is determined by a user input of the respective first letters. The dictionary has been parsed into subdictionaries for each difficulty, and which subdictionaries that are removed are determined by the input. If you're playing on Easy, you dont need any of the items from Medium or Hard, do you? It also removes the first element of the dictionary, where it tells the difficulty. Don't want that interfering because it's not data we'll use. The ~~hard~~ technical part comes in when the All difficulty is selected. It still deletes the difficulty settings of each subdictionary, but then creates a whole new and separate dictionary where the subdictionaries are combined into one. A new element is created in the original dictionary with "4" being the difficulty level and the value is the total dictionary. The length of the selected dictinary is recorded as the number of items for later purposes.
#### Rounds
A While loop is run to get input from the user for the number of rounds. It must be a whole number between 1 and the number of items from just above. If the user inputs anything else, it will continue to ask for a valid number.
#### Confirmation
The user selects to be tested on the PLUs or Names, and must type "Y" (for "yes") as confirmation to start the test.
#### Generation and Checking
A list of random PLUs is generated using the standard library [random.sample()](https://docs.python.org/2/library/random.html#random.sample). I make a list of the difficulty's keys and pass that as the population parameter, and pass the number of rounds as the parameter for how many items to populate the list with. This list is effectively the answer key. There is a simple For loop ran to generate the PLU, and asks the user what the PLU of the name is. The answer is checked against the user's input. If the strings match, a correct point is awarded and a message saying "Correct" is displayed, along with a ratio of correct/total answered. If the strings do not match, an "Incorrect" message is displayed and the user will not be awarded a correct point. This process repeats for each PLU in the randomly generated list. After the last PLU is checked, a total score will be displayed for that session and the program will exit.
#### v0.2 - Names
I do the same thing as I did with creating a random list as the answer key, but with the difficulty's values as the population. The only thing I did different was once I got this list, it runs a For loop to find the key (PLU) based on if the generated name matches the value of the key. Once it has a confirmed match, it parses the value into a readable format, replacing underscores with spaces. It compares "answer" to the user input, and counts to number correct out of the total questions already asked.
