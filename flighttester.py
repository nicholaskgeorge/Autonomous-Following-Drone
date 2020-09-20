from message import Messages
from fccontrolclass import FlightControllerCommands as fc

message = Messages('Laptop',topic="test/message")
message.start()
control  = fc()
control.start()

while True:
    if message.received == 'up':
        control.throttle += 10
    if message.received == 'down'
        control.throttle -= 10
