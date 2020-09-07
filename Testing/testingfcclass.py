import sys
sys.path.append(r'/home/pi/Desktop/Autonomous-Following-Drone/')
from fccontrolclass import FlightControllerCommands

drone = FlightControllerCommands(throttle = 1100)
drone.start()
sleep(10)
drone.constantmessage=False
