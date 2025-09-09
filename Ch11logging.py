import logging
import random
import sys
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')



logging.debug('Start of program')

try:
    import data
#   from data import *  
    logging.debug("myfile loaded successfully")
except:
    print("My file is missing! Program will exist now.")
    logging.debug("myfile.py is missing! Investigate!")
    sys.exit()

logging.info('End of program')

