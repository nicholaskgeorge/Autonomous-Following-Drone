import sys
import time
sys.path.append(r'/home/pi/Desktop/Autonomous-Following-Drone/')
from messaging import Messages

remote = Messages(clientname = 'Get',broker = "10.49.12.253", topic = "test/message")
remote.begin()
remote.end()
