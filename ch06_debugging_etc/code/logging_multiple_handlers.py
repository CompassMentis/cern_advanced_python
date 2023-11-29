import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('demo.log', 'w')
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)

terminal_handler = logging.StreamHandler()
terminal_handler.setLevel(logging.DEBUG)
logger.addHandler(terminal_handler)

logger.debug('a = 10')
logger.info('10% disk space remaining')
logger.warning('5% memory remaining')
logger.error('ZeroDivisionError')

# Output to terminal
# a = 10
# 10% disk space remaining
# 5% memory remaining
# ZeroDivisionError

# Output to demo.log
# 5% memory remaining
# ZeroDivisionError
