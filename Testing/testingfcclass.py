import sys
sys.path.append(r'/home/pi/Desktop/Autonomous-Following-Drone/')
from fccontrolclass import FlightControllerCommands
from time import sleep

drone = FlightControllerCommands(throttle = 855, yaw = 1700, roll = 1000)
drone.start()
for i in range(845):
    drone.throttle+=1
    sleep(0.03)
drone.constantmessage=False
