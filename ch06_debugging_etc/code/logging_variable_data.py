import logging

logging.basicConfig(level=logging.INFO)

error_value = 25
logging.error('Error %s', error_value)
# ERROR:root:Error 25
