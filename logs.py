import logging
from logging.handlers import RotatingFileHandler

class Logger:

    def __init__(self, log_file="logs/app.log", level=logging.DEBUG):

        # Configure logger
        self.logger = logging.getLogger("AppLogger")
        if not self.logger.handlers: 
            self.logger.setLevel(level)
            
            # Formatter for log messages
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s", 
                "%Y-%m-%d %H:%M:%S"
            )
            
            # File handler with rotation
            file_handler = RotatingFileHandler(
                log_file, mode='w', maxBytes=5 * 1024 * 1024, backupCount=1  # 5 MB per file, 3 backups
            )
            file_handler.setFormatter(formatter)
            
            # Stream handler (console logs)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            
            # Add handlers to the logger
            self.logger.addHandler(file_handler)
            # self.logger.addHandler(console_handler)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)
