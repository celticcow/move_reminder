#!/usr/bin/python3

import time
from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(title="Mobility", message="Chin Tuck x 10", timeout = 10)
        time.sleep(7200)
    #end of while
#end of program