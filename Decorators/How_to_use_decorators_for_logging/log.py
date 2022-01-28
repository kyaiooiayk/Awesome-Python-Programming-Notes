import logging
import os
import shutil

def get_logger(log_file_name, log_dir=""):
    """Creates a Log File and returns Logger object     
    
    Create Log file directory if not exists
    """

    # Build Log File Full Path
    logPath = log_file_name if os.path.exists(log_file_name) else os.path.join(log_dir, (str(log_file_name) + '.log'))
    
    
    # Create handler for the log file
    #================================
    # Create logger object and set the format for logging and other attributes                           
    logger = logging.Logger(log_file_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(logPath, 'a+')    
    formatter = logging.Formatter('%(asctime)s | %(levelname)s %(message)s', '%Y/%m/%d | %H:%M:%S')
    # ('%(asctime)s - %(levelname)-10s - %(filename)s - %(levelname)s - %(message)s'))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    # Create handler for the console output
    #======================================
    # Define a Handler which writes INFO messages or higher to the sys.stderr
    console=logging.StreamHandler()
    console.setLevel(logging.INFO)
    # Set a console format which is esier to read
    formatter=logging.Formatter('%(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # Add the handler to the root logger    
    logger.addHandler(console)
                  
    # Return logger object
    return logger
 