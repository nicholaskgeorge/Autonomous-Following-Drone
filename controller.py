from messaging import Messages
from fccontrolclass import FlightControllerCommands as fc
from time import perf_counter
from time import sleep

"""
This is a small file that I am using to test the drone and control it.
For now I can only throttle up and down. In the future I will likley use something
like ROS the handle this logic
"""
message = Messages('control',topic="test/message")
message.start()
drone = fc(throttle = 1000, yaw = 1500, roll = 1500)
drone.disarm()
drone.arm()
drone.start()
old = ''
while True:
    sincelastmessage = perf_counter()-message.timerecived
    if sincelastmessage>2:
        drone.mode = "land"
    news = message.received
    if news != old:
        print (news)
        old = news
    if drone.mode = "armed":
        if news == 'up' and drone.throttle <2000:
            drone.throttle +=5
        elif news == 'down'and drone.throttle>1000:
            drone.throttle -=5
        elif news == 'forward':
            drone.pitch = 1520
        elif news == 'backward':
            drone.pitch = 1480
        elif news == 'right':
            drone.roll = 1520
        elif news == 'left':
            drone.roll = 1480
        else:
            drone.pitch = 1500
            drone.roll = 1500
    elif drone.mode = "land":
        while drone.throttle>1000:
            drone.pitch = 1500
            drone.roll = 1500
            drone.throttle -= 5
            sleep(0.005)
        drone.constantmessage = False

    sleep(0.03)
