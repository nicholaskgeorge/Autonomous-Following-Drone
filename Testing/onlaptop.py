from messaging import Messages

remote = Messages()
remote.begin()
remote.send("test/message",'This is the first real sucess')
