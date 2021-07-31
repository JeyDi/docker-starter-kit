from logger import logger
from mymodule.name_selector import name_parsing

if __name__ == "__main__":
    logger.info("Starting the program...")

    name = input("Please Enter Your Name: \n")

    name_parsing(name)

    logger.debug("program launched correctly! ;)")

    logger.info("finish..")
