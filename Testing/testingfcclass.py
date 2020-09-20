import sys
sys.path.append(r'/home/pi/Desktop/Autonomous-Following-Drone/')
from fccontrolclass import FlightControllerCommands
from time import sleep

drone = FlightControllerCommands(throttle = 1000, yaw = 1500, roll = 1500)
drone.disarm()
drone.start()
for i in range(400):
    drone.throttle+=1
    sleep(0.03)
drone.constantmessage=False
