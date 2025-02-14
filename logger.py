import logging
import time
import os

Debug = False # control the logger output, if ture then send the debug message

'''
Setting the logger and save the log to file
'''
logFileFolder = "log/"
if not os.path.exists(logFileFolder):
    os.mkdir(logFileFolder)

logFileName = time.strftime("%Y%m%d%H%M%S", time.localtime())

logger = logging.getLogger()
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename=f"{logFileFolder + logFileName}.log", encoding="utf-8")
logger.addHandler(console_handler)
logger.addHandler(file_handler)
#formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
if Debug:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
