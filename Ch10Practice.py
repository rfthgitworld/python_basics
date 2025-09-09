from pathlib import Path
import os
import pprint
import shutil
import send2trash
import zipfile

# p = Path.cwd()

# # shutil.copy(p / 'test2.txt', p / 'testdir')
# shutil.copy(p / 'test2.txt', p / 'testdir/test_copy.txt')

# shutil.copytree(p / 'testdir', p / 'testdir_bk')

# shutil.move(p / 'testdir/test_copy.txt', p / 'testdir_bk')

# shutil.move(p / 'testdir/test2.txt', p / 'testdir_bk/new_test.txt')

# os.unlink(p / 'testdir_bk/test_copy.txt')

# os.rmdir(p / 'testdir_bk')

# shutil.rmtree(p / 'testdir_bk')


# send2trash.send2trash(p / 'testdir')

# p = Path(r'C:\Users\rifat\OneDrive\Documents\IT\python')

# for folderName, subfolders, filenames in os.walk(p):
#     print('The current folder is ' + folderName)
     
#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': '+ filename)

#     print('')


# p = Path(r'C:\Users\rifat\OneDrive\Documents\IT\python\python_intro\INF360')

# p = Path.cwd()

# exampleZip = zipfile.ZipFile(p / 'test.zip')
# # list = exampleZip.namelist()
# # print(list)
# # info = exampleZip.getinfo('test.txt')
# # print(info.file_size)

# # exampleZip.extractall()
# # exampleZip.close()

# newZip = zipfile.ZipFile('test2.zip', 'w')
# newZip.write('test2.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()


# newZip = zipfile.ZipFile('test2.zip', 'a')
# newZip.write('test.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()


# listZip = zipfile.ZipFile(p / 'test2.zip')
# list = listZip.namelist()
# print(list)


# import bext
# bext.fg('red')
# print('This text is red.')

# bext.bg('blue')
# print('Red text on blue background is an ugly color scheme.')

# bext.fg('reset')
# bext.bg('reset')
# print('The text is normal again. Ah, much better.')
