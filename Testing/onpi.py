import sys
import time
sys.path.append(r'/home/pi/Desktop/Autonomous-Following-Drone/')
from messaging import Messages

remote = Messages('Drone')
remote.begin()
remote.startsub("test/message")
remote.client.loop_forever()
while True:
    print(remote.received)
    time.sleep(0.8)
