import serial
from time import sleep
import struct
import threading

class FlightControllerCommands(threading.Thread):
    """
    This is a class which allows for the communication between the pi and any flight
    controller which supports serial communication in the ibus format. When the thread
    is started it will send serial messages to the flight controller 142 times per second
    """
    def __init__(self, port = '/dev/ttyS0', throttle=885, pitch=1500, yaw=1500, roll=1500):
        super().__init__()
        self.port = port
        self.throttle = throttle
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll
        self.connected = False
        self.constantmessage = False
        self.mode = "disarmed"
        self.senddelay = 0.01
    def connecttoport(self,dport):
        """This function connect to the desired port"""
        port= serial.Serial(dport,115200, timeout=10, write_timeout=10)
        print("Desired port is "+port.name)
        self.connected = port
        return port
    def send(self, dmsg, port):
        """This function is what is used to send the final message. It takes the port
        you want and the message as arguments."""
        port.write(dmsg)
    def pack(self, channels):
        """This function packs the desired message in the ibus format. You give it the
        values for all 14 channel in an array. Unused channels must be given the
        value 0x05DC"""
        message=[]

        #adds the required begining header of the message
        message.append(0x20)
        message.append(0x40)
        #puts each channel value in little endian format in the message
        for channel in channels:
            message.append(channel%256)
            message.append(channel//256)
        #calculates and ands the required cheksum
        msgsum=0
        for i in message:
            msgsum+=i
        checksum = 0xffff-msgsum
        message.append(checksum%256)
        message.append(checksum//256)
        #ensures each of the two parts of each channel is 1 byte by converting it to
        #a char
        return message #list(map(lambda i :st
    def commands(self, channels):
        """This function will take any amount of channels given and both pack and send
        the message to the flight controller. Values given must still be given in the
        order of the channels"""
        command = []
        for i in channels:
            command.append(i)
        command+=([1000]*(14-len(channels)))
        message = self.pack(command)
        # with connecttoport('/dev/ttyS0') as port:
        #     print (channels)
        #     send(message, port)
        # print(channels)
        # print(len(message))
        # print(max(message))
        if self.connected:
            self.send(message, self.connected)
        else:
            self.send(message, self.connecttoport('/dev/ttyS0'))
    def disarm(self):
        print("Disarming Drone")
        self.mode = "disarmed"
        for i in range(600):
            sleep(self.senddelay)
            self.commands([1500, 1500,885,1500, 1500])
    def arm(self):
        print("Arming Drone")
        self.mode = "armed"
        for i in range(600):
            sleep(self.senddelay)
            self.commands([1500, 1500, 1000, 1500, 1200])
    def run(self):
        self.constantmessage = True
        print('Begining communications with flight controller')
        while self.constantmessage:
            self.commands([self.roll,self.pitch,self.throttle,self.yaw,1200])
            sleep(self.senddelay)
            #sleep(0.007)
        print('Ending communication')
