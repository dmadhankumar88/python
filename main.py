import logging
import Addition
import Subtraction

# Configure Logging System
logging.basicConfig(
    level=logging.DEBUG,  # Set log level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Define log format
)

# Create a logger for main.py
logger = logging.getLogger(__name__)

logger.info("Application started")

# Call functions from other modules
result1 = Addition.process_numbers(10, 5)
result2 = Subtraction.calculate_difference(20, 8)

logger.info("Application finished")
