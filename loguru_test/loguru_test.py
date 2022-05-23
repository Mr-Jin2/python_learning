
from loguru import logger
logger.add('runtime.log')
logger.remove(handler_id=None)

logger.debug("this is a debug msg")
