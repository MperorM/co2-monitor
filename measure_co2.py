import mh_z19
import time

while True:
    log = open('log.txt', 'a+')
    for i in range(0,5):
        mh_z19.read_all()
        time.sleep(0.5)
        reading = mh_z19.read_all()
        timestamp = time.localtime()
        #log.write(str(timestamp.tm_hour) + '.' + str(timestamp.tm_min) + ": " + str(reading) + '\n')
        print(str(timestamp.tm_hour) + '.' + str(timestamp.tm_min) + ": " + str(reading) + '\n')
        time.sleep(1)
    log.close()
