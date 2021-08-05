import schedule
import time

from logger import logger
from cron.utils.func import test_job

if __name__ == "__main__":

    logger.info(" --- Schedule Cron Job Test --- ")

    # Register the job you want to launch
    # schedule.every(1).minutes.do(launch_operations())
    schedule.every().day.at("00:30").do(test_job())

    # Launch the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)
