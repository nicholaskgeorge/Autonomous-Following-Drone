sys.path.append(r'/home/pi/Desktop/Autonomous-Following-Drone/')
from messaging import Messages
remote = Messages()
remote.begin()
remote.startsub("test/message")
while True:
    print(remote.received)
    time.sleep(0.8)
