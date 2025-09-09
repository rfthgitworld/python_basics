'''
INF360 - Programming in Python

Assignment 4

I,  Rifat Hossain  , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized
materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor
received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions
as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

'''

# (1/1 point) - Initial comments*
# (2/2 points) - Read the file story.txt and store the lines as a variable called story.You must use relative paths, assume the story.txt file is in the same folder as your script.
# (5/5 points) - Write a regular expression that will find all occurrences of the phrase, "Sherlock Holmes".
# (5/5 points) - Using the substitue method, replace all occurrences of "Sherlock Holmes" with your name, storing the count of these occurrences as a variable called foundCount.
# (2/2 points) - Write a regular expression that will find all occurrences of the phrase, "the".
# (3/3 points) - Create a variable called theCount, that stores the total number of occurrences of the phrase "the".
# (3/3 points) - Print to the user, the original name, the replacement name, and the total number of occurrences using a print command with a formatted string literal using a string that starts with f".
# (3/3 points) - Print to the user the a string that tells the user the total number of occurrences of "the" using a print command with a formatted string literal using a string that starts with f".
# (1/1 points) - Save the story out to a new file called new_story.txt.


from pathlib import Path
import os
import re
import send2trash

# Read the story.txt file to lines from a relative path and storing the result in a variable called "Story".
readFile = open('story.txt')
story = readFile.readlines()
readFile.close()


# Diclared two variables for Originial Name and New Name.
orgName = "Sherlock Holmes"
newName = "Rifat Hossain"

# Created a regular expression that will find all occurrences of the phrase, "Sherlock Holmes".
findSherlock =  re.compile(orgName)

# Storing the count of occurrences of "Sherlock Holmes" as a variable called foundCount.
foundCount = len(findSherlock.findall("".join(story)))

# Using the substitute method, replaced all occurrences of "Sherlock Holmes" with my Name "Rifat Hossain".
replaceName = findSherlock.sub(newName, "".join(story))


# Created a regular expression that will find all occurrences of the phrase, "the".
theMatches = re.compile(r'\bthe\b')

# created a variable called theCount, that stores the total number of occurrences of the phrase "the".
theCount = len(theMatches.findall("".join(story)))

# Prints to the user, the original name, the replacement name, and the total number of occurrences using a print command with a formatted string literal using a string that starts with f".
print("")
print(f'The original name was {orgName}, and the new name is {newName}. The total number of occurrences of "Sherlock Holmes" in the story is {foundCount}.')

# Prints to the user the a string that tells the user the total number of occurrences of "the" using a print command with a formatted string literal using a string that starts with f".
print(f'Total number of occurrences of "the" in the story is {theCount}.')
print("")

# Saves the story out to a new file called new_story.txt and removes any pre-existing "new_story.txt" file. 
if os.path.exists('new_story.txt'):
    send2trash.send2trash('new_story.txt')
    
newStory = open('new_story.txt', 'w')
newStory.write(replaceName)
newStory.close()

######## End of the program ##########