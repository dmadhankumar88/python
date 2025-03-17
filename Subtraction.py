import logging
from utils import subtract

# Create a logger for module_b
logger = logging.getLogger(__name__)

def calculate_difference(a, b):
    logger.debug(f"Calculating difference between {a} and {b}")
    result = subtract(a, b)
    logger.info(f"Difference: {result}")
    return result
