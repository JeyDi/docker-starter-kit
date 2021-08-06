import time

from logger import logger
from cron import test_job

if __name__ == "__main__":

    logger.info(" --- Launching CronTab Job --- ")
    
    test_job()
    time.sleep(1)
    
    logger.info(" Cron finished ")
    
