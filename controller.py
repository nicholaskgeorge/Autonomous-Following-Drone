from messaging import Messages
from fccontrolclass import FlightControllerCommands as fc
from time import sleep
message = Messages('control',topic="test/message")
message.start()
drone = fc(throttle = 1000, yaw = 1500, roll = 1500)
drone.disarm()
drone.arm()
drone.start()

while True:
    news = message.received
    if news == 'up' and drone.throttle <2000:
        drone.throttle +=5
    if news == 'down'and drone.throttle>1000:
        drone.throttle -=5
    sleep(0.05)
