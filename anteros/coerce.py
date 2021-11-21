#!/usr/bin/python3
# -*- coding: utf-8 -*-

__version__ = "1.0.0"

# Local Imports

# Repo Imports
import os
import sys

# Load Properties
from anteros import properties

# Setuop Logger
import logging
from logging import config as logging_config
logging_config.fileConfig(properties.LOGGING_CONFIG)
logger = logging.getLogger(__name__)

# Main
def main():
    logger.info('Hey, that was easy as 123')

# Set the entry point
if __name__ == '__main__':
    main()