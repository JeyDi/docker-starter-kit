import random

from cron.logger import logger

def test_job(length:int = 100, min_gen: int= 10, max_gen: int = 30):
    logger.debug("Generating numbers...")
    #Generate random numbers
    randomlist = random.sample(range(min_gen, max_gen), length)
    
    return randomlist
    