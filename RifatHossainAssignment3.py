'''
INF360 - Programming in Python

Assignment 3

I,  Rifat Hossain  , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized
materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor
received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions
as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

'''

# (1/1 points) Initial Comments.
# (5/5 points) Create a dictionary for each vehicle that contains the fields/keys and values listed above.
# (5/5 points) Write a function that will take a list of these dictionaries and return a new dictionary with the 'name' value as the key, and the dictionary as the value.
# (5/5 points) Write a function that will go through the newly created dictionary and return a list of all the car's names, sorted alphabetically.
# (5/5 points) Write a function that will go through the newly created dictionary return a dictionary of all the cars names and year introduced.
# (5/5 points) Use a print statement to show the results of the function from step 3, each on their own line.
# (5/5 points) Use a print statement to show the results of the function from step 4 to display in the format: year : name. Sort by year introduced.



# Dictionaries for each vehicle found in the Ford data table.

car1 = {
    "Name": "Ka",
    "Year Introduced": "1996",
    "Production of the Current Model": "2014",
    "Generation": "3rd",
    "Vehicle Information": "Developed by Ford Brazil as a super mini car"
} 

car2 = {
    "Name": "Fiesta",
    "Year Introduced": "1976",
    "Production of the Current Model": "2017",
    "Generation": "7th",
    "Vehicle Information": "Ford's long running subcompact line based on global B-car Platform"
}

car3 = {
    "Name": "Focus",
    "Year Introduced": "1998",
    "Production of the Current Model": "2018",
    "Generation": "3rd",
    "Vehicle Information": "Ford's Compact car based on global C-car platform"
}

car4 = {
    "Name": "Mondeo",
    "Year Introduced": "1992",
    "Production of the Current Model": "2012",
    "Generation": "2nd",
    "Vehicle Information": 'Mid sized passenger sedan with "One-Ford" design based on CD4 platform'
}

car5 = {
    "Name": "Fusion",
    "Year Introduced": "2005",
    "Production of the Current Model": "2014",
    "Generation": "5th",
    "Vehicle Information": "Similar to Mondero"
}

car6 = {
    "Name": "Taurus",
    "Year Introduced": "1986",
    "Production of the Current Model": "2009",
    "Generation": "6th",
    "Vehicle Information": "Full sized car based on D3 platform"
}

car7 = {
    "Name": "Fiesta ST",
    "Year Introduced": "2013",
    "Production of the Current Model": "2013",
    "Generation": "1st",
    "Vehicle Information": "Fiesta's high performance factory tune"
}

car8 = {
    "Name": "Focus RS",
    "Year Introduced": "2015",
    "Production of the Current Model": "2015",
    "Generation": "1st",
    "Vehicle Information": "Special high performance Focus developed by SVT"
}

car9 = {
    "Name": "Mustang",
    "Year Introduced": "1964",
    "Production of the Current Model": "2014",
    "Generation": "6th",
    "Vehicle Information": "Ford's long running pony/muscle car"
}

car10 = {
    "Name": "GT",
    "Year Introduced": "2004",
    "Production of the Current Model": "2016",
    "Generation": "2nd",
    "Vehicle Information": "Ford's limited production super car inspired by the legendary race car GT40"
}

# A List for the dictionaries above 

cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]

# step 3: Write a function that will take a list of these dictionaries and return a new dictionary with the 'name' value as the key, and the dictionary as the value.

def newdictionary (carlist):
    newdict = {}
    for car in carlist:
        newdict[car["Name"]] = car
    return newdict
          
# Step 4: Write a function that will go through the newly created dictionary and return a list of all the car's names, sorted alphabetically.
    
def sortedlist (newdict):
    
    # Get all the keys (car names) from the dictionary and convert it using list () fucntion
    carnames = list(newdict.keys())
    
    # Sort the list alphabetically
    carnames.sort()
    
    # assign the sorted list to result
    result = carnames
    return result
  

# Step 5: Write a function that will go through the newly created dictionary return a dictionary of all the cars names and year introduced.

def car_details (newdict):
    result = {}
    for details in newdict.values():
        result[details["Name"]] = details["Year Introduced"]
    return result

# Step 6: Use a print statement to show the results of the function from step 3, each on their own line.

for name, info in newdictionary(cars).items():
    print(f"{name}: {info}")
    
# Step 7: Use a print statement to show the results of the function from step 4 to display in the format: year : name. Sort by year introduced.

car_info = car_details(newdictionary(cars))

# Flip the key-value order to (year, name)
car_list = [(year, name) for name, year  in car_info.items()]

car_list.sort()

for year, name in car_list:
    print(f"{year} : {name}")
    
    
