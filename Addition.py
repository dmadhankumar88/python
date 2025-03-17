import logging
from utils import add

# Create a logger for module_a
logger = logging.getLogger(__name__)

def process_numbers(x, y):
    logger.debug(f"Processing numbers {x} and {y}")
    result = add(x, y)
    logger.info(f"Result: {result}")
    return result
