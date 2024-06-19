import logging
import os
import inspect

def get_default_log_filename():
    # Get the filename of the calling script
    caller_frame = inspect.stack()[-1]
    caller_script = os.path.basename(caller_frame.filename)
    log_filename = f"{os.path.splitext(caller_script)[0]}.log"
    return log_filename

def printx_configure(log_filename=None, level=logging.DEBUG):
    if log_filename is None:
        log_filename = get_default_log_filename()

    logging.basicConfig(level=level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler(log_filename),
                            logging.StreamHandler()
                        ])

def printx(*args, log_level='info', **kwargs):
    message = ' '.join(map(str, args))
    
    if log_level == 'debug':
        logging.debug(message)
    elif log_level == 'info':
        logging.info(message)
    elif log_level == 'warning':
        logging.warning(message)
    elif log_level == 'error':
        logging.error(message)
    elif log_level == 'critical':
        logging.critical(message)
    else:
        logging.info(message)
