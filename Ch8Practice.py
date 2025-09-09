from pathlib import Path
import os
import pprint


# print(Path.cwd())

# os.chdir('c:/Users/rifat/OneDrive/Documents/IT/python/python_intro')
# print(Path.cwd())

# print(Path.home())

# os.makedirs('c:/Users/rifat/OneDrive/Documents/IT/python/python_intro/new_dir')  # better option

# or

# Path(r'c:/Users/rifat/OneDrive/Documents/IT/python/python_intro/new_dir').mkdir()

# print(Path.cwd().is_absolute())

# p = Path('IT/python/python_intro')
# print(p.is_absolute())

p = Path.cwd()
# print(Path.cwd())
# print(os.path.basename(p))
# print(os.path.dirname(p))
# print(os.path.split(p))

# print(os.path.getsize(r'C:\Users\rifat\OneDrive\Documents\IT\python\python_intro\INF360\RifatHossainAssignment1.py'))


# p = Path.cwd()
# listdir = os.listdir(p)
# results = []
# for filename in listdir:
#     line = f"Filename: {filename.ljust(30, ' ')} Size: {round((os.path.getsize(p / filename)/1024), 1)} {'KB'.rjust(1, ' ')}"
#     results.append(line)

# fileObj = open('filesize.txt', 'w')
# fileObj.write(pprint.pformat(results) + '\n')
# fileObj.close()




# for line in results:
#     print(line)
    
# p= Path('c:/Users/rifat/OneDrive/Documents/IT/python/python_intro')
# # a = list(p.glob('*loop*'))
# print(a)

# if p.exists():
#     print("True")
    
# if p.is_dir():
#     print("True")
    
# if p.is_file():
#     print("Ture")
# else:
#     print("It's not a file")
    
# p = Path('test.txt')
# p.write_text('Hello World!')
# print(p.read_text())

# p = open('test.txt')
# print(p.readlines())
# p.close()

# p = open('test.txt')
# print(p.read())
# p.close()


# p = open('test2.txt', 'w')
# p.write("It's easy to learn.\n")
# p.close()

# p = open('test.txt', 'a')
# p.write("It's easy to learn.\n")
# p.close()


cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

print(pprint.pformat(cats))

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

fileObj = open('myCats.py')
print(fileObj.read())

# import myCats

# print(myCats.cats)