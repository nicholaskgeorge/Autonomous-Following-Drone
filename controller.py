from messaging import Messages
from fccontrolclass import FlightControllerCommands as fc
from time import sleep

"""
This is a small file that I am using to test the drone and controll it.
For now I can only throttle up and down. In the future I will likley use something
like ROS the handle this logic
"""
message = Messages('control',topic="test/message")
message.start()
drone = fc(throttle = 1000, yaw = 1500, roll = 1500)
drone.disarm()
drone.arm()
drone.start()

while True:
    news = message.received
    print(news)
    if news == 'up' and drone.throttle <2000:
        drone.throttle +=5
    if news == 'down'and drone.throttle>1000:
        drone.throttle -=5
    sleep(0.03)
