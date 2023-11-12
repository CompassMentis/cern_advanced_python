import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

logger.setLevel(logging.INFO)
logger.info('Some information')  # Some information
logger.debug('Debug data')       # (no output)

logger.setLevel(logging.DEBUG)
logger.info('Some information')  # Some information
logger.debug('Debug data')       # Debug data

formatter = logging.Formatter('[%(levelname)s] %(message)s')
stream_handler.setFormatter(formatter)
logger.info('Some information')  # [INFO] Some information
