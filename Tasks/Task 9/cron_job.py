# As there is no cron job in windows. We can use Schedule to run a script in time

import schedule
import time
counter = 0
def task():
    global counter
    print("The counter NOW = " , counter )
    counter+=1
    

schedule.every(1).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)