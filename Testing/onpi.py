from messaging import Messages

remote = Messages()
remote.begin()
remote.startsub("test/message")
while True:
    print(remote.received)
