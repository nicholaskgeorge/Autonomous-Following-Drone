import sys
sys.path.append(r'C:\Users\Nico\Autonomous-Following-Drone')
from messaging import Messages
import time

remote = Messages('Laptop', topic = "test/message")
remote.begin()
remote.send('This is the first sucess')
time.sleep(2)
remote.send('Seeing if this works')
remote.end()
