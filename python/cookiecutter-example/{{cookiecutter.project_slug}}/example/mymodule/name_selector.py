from logger import logger
from config import SPAGHETTI


def name_parsing(name: str = None) -> str:

    if name is None:
        logger.error(f"Name: {name} not valid, please retry..")
        logger.exception("Name not valid..")

    logger.info(f"Hello: {name.strip().lower()}, welcome here!")
    logger.debug(f"So do you like: {SPAGHETTI} right?")

    return name
