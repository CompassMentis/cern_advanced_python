import logging

logging.basicConfig(level=logging.INFO)

# Levels, in increasing order
logging.critical('Critical error, level 50')
logging.error('Error, something happened, level 40')
logging.warning('Warning, be careful, level 30')
logging.info('Info, just to let you know, level 20')
logging.debug('Some debug output, level 10')

# Output
# CRITICAL:root:Critical error, level 50
# ERROR:root:Error, something happened, level 40
# WARNING:root:Warning, be careful, level 30
# INFO:root:Info, just to let you know, level 20

# Note: .debug not shown, below the .INFO level
