# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)


# import pyperclip

# pyperclip.copy('Hello, world!')
# print(pyperclip.paste())


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


cars = [car1, car2]

print(cars)

def cardetails (carlist):
    for k, v in carlist.items():
        print (k, v)
        
cardetails(cars)