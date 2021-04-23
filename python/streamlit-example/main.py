import logging
import streamlit as st
import src.dashboard.menu as main_menu
from src.config import VERBOSITY
from logging.handlers import RotatingFileHandler

# Set Logs settings
# Set verbosity
log_level = level = logging.getLevelName(VERBOSITY.upper())
if isinstance(log_level, int):
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)s] %(asctime)s | %(message)s | in function: %(funcName)s",
        handlers=[
            RotatingFileHandler("info.log", maxBytes=10000, backupCount=10),
            logging.StreamHandler(),
        ],
    )
elif VERBOSITY == "info":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(asctime)s | %(message)s | in function: %(funcName)s",
        handlers=[
            RotatingFileHandler("info.log", maxBytes=10000, backupCount=10),
            logging.StreamHandler(),
        ],
    )

if __name__ == "__main__":
    #create the dashboard heading    
    main_menu.launch()