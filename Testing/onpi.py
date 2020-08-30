from messaging import Messages
sys.path.append(r'/home/pi/Desktop/Autonomous-Following-Drone/')
remote = Messages()
remote.begin()
remote.startsub("test/message")
while True:
    print(remote.received)
    time.sleep(0.8)
