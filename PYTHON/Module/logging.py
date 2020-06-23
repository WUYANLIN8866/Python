import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
logger.debug(1)
logger.info(2)
logger.warning(3)
logger.error(4)
logger.critical(5)
# NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL