from loguru import logger


def setup_logger():
    logger.remove()  # Remove the default logger
    logger.add(
        "logs/api.log",  # Log file path
        rotation="1 MB",  # Rotate log file when it reaches 1 MB
        retention="7 days",  # Keep logs for 7 days
        level="TRACE",  # Log level
        format="{time} {level} {message}",  # Log format
    )
    return logger

# Initialize the logger
logger = setup_logger()

# Example usage:
# from api.utils.logger import logger
# logger.info("Logger is set up and ready to use.")
