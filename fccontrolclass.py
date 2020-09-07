import serial
from time import sleep
import struct

class FlightControllerCommands(threading.Thread):
    def __init__(port = '/dev/ttyS0', throttle=885, pitch=1500, yaw=1500, roll=1500):
        self.port = port
        self.throttle = throttle
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll
        self.connected = False
        self.constantmessage = False
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
        if connected:
            self.send(message, self.connected)
        else:
            self.send(message, self.connecttoport('/dev/ttyS0'))
    def run(self):
        print('Begining communications with flight controller')
        while constantmessage:
            commands([1500,1500,1500,885])
            sleep(0.007)
        print('Ending communication')
