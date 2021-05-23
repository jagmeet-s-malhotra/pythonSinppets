#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 00:15:19 2021
# https://medium.com/swlh/python-async-logging-to-an-elk-stack-35498432cb0a
# Data from Kaggle
@author: Jagmeet Singh Malhotra
"""
import logging
import random
import time
from logstash_async.handler import AsynchronousLogstashHandler
host = 'localhost'
port = 5000
# Get you a test logger
test_logger = logging.getLogger('python-logstash-logger')
# Set it to whatever level you want - default will be info
test_logger.setLevel(logging.DEBUG)
# Create a handler for it
async_handler = AsynchronousLogstashHandler(host, port, database_path=None)
# Add the handler to the logger
test_logger.addHandler(async_handler)





def get_aValue():
        filesize = 150               #size of the really big file
        offset = random.randrange(filesize)

        f = open('./StockData.csv')
        f.seek(offset)                  #go to random position
        f.readline()                    # discard - bound to be partial line
        random_line = f.readline()      # bingo!

        # extra to handle last/first lsine edge cases
        if len(random_line) == 0:       # we have hit the end
            f.seek(0)
            random_line = f.readline()  # so we'll grab the first line instead
        
        return random_line


def main():
    while True:
        level = ['Info', 'Warning', 'Error', 'FATAL', 'TRACE', 'DEBUG']
        message = random.choice(level) + ' : '+get_aValue()
        test_logger.info(message)
        time.sleep(5)
    
if __name__ == "__main__":
    main()