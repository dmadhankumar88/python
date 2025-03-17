import logging

# Create a logger for this module
logger = logging.getLogger(__name__)

def add(a, b):
    logger.info(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    logger.info(f"Subtracting {a} - {b}")
    return a - b
