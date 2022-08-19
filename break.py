#!/usr/bin/python3

import time
from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(title="Alert", message="go walk for a min", timeout = 10)
        time.sleep(60)
    #end of while
#end of program