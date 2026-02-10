# Logging Utility

A Python application demonstrating centralized logging implementation using rotating file handlers.

## Features

- **Centralized Logging**: Reusable `Logger` class for consistent log management
- **Rotating File Handler**: Automatic log rotation at 5MB with backup retention
- **Multiple Log Levels**: Support for DEBUG, INFO, WARNING, ERROR, and CRITICAL levels
- **Structured Format**: Timestamped log entries with clear formatting

## Project Structure

```
├── app.py          # Main application with LogChecker class
├── logs.py         # Logger utility class
└── logs/           # Log files directory
    └── app.log     # Application logs
```

## Usage

```python
from logs import Logger

logger = Logger()
logger.log_info("Application started")
logger.log_error("An error occurred")
```

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## Configuration

Default settings in `Logger` class:
- **Log File**: `logs/app.log`
- **Max File Size**: 5MB
- **Backup Count**: 1
- **Log Level**: DEBUG

Modify these parameters during initialization as needed.
