
import sys, os, functools
from inspect import getframeinfo, stack
import log
import logging

def logger(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        """Logger function decorator
        
        Takes care of both the dumped .log file
        and the console ouput. The rule used here is as follows:
        - Only general and DEBUG information are log inside the decorator.
        - Anything else is logged inside the funciton being called.
        """
        
        # Create logger object
        logger_obj = log.get_logger(log_file_name=self.log_file_name, log_dir=self.log_file_dir)
        
        # This is a series of general info applicable to any methods/functions
        logger_obj.debug("\n")
        logger_obj.debug("Enter method")                
        logger_obj.debug("Method's name: " + func.__name__)
        logger_obj.debug("Method's args: {}".format(args))
        logger_obj.debug("Method's kwargs: {}".format(kwargs))        
        
        # Call the function as usual
        value = func(self, *args, **kwargs)        
        logger_obj.debug("Exit method")
        logger_obj.debug("\n")
        
        return value

    return wrapper
