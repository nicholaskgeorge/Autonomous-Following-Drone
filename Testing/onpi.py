import sys
import time
sys.path.append(r'/home/pi/Desktop/Autonomous-Following-Drone/')
from messaging import Messages

remote = Messages(clientname = 'Get',broker = "10.49.12.253", topic = "test/message")
remote.start()
while remote.received!='Please end':
    print(remote.received)
    time.sleep(3)
remote.end()
