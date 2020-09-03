import sys
import time
sys.path.append(r'/home/pi/Desktop/Autonomous-Following-Drone/')
from messaging import Messages

remote = Messages(clientname = 'Drone',broker = "localhost", topic = "test/message")
remote.begin()
remote.end()
