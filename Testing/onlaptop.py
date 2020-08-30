import sys
sys.path.append(r'C:\Users\Nico\Autonomous-Following-Drone')
from messaging import Messages

remote = Messages()
remote.begin()
remote.send("test/message",'This is the first real sucess')
