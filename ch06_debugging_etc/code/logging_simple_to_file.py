import logging

logging.basicConfig(
    level=logging.INFO,
    filename='demo.log'
)
logging.warning('Hello')
logging.debug('test')

# Result, contents of demo.log:
# WARNING:root:Hello
