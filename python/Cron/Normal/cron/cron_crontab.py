from logger import logger
from crontab import CronTab  

if __name__ == "__main__":

    logger.info(" --- Configuring the CronTab --- ")

    cron = CronTab(user='username') 
    task = cron.new(command='python cron/run-crontab.py') 
    task.minute.every(2)
    #task.month.during('MAR', 'APR')
    cron.write()
