import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

logger.error('Out of diskspace')
# [2023-11-07 18:50:42,359, ERROR] Out of diskspace
