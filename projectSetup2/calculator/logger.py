import logging

# Configure logging
logging.basicConfig(
    filename="app.log",  # Log file name
    level=logging.INFO,  # Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Create a logger instance
logger = logging.getLogger(__name__)

# Example log messages
logger.info("Logger initialized successfully.")
