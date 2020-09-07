import serial
from time import sleep
import struct
from time import sleep

"""variable which tells if we have already connected to the serial port"""
connected = None

def connecttoport(dport):
    global connected
    """This function connect to the desired port"""
    port= serial.Serial(dport,115200, timeout=10, write_timeout=10)
    print("Desired port is "+port.name)
    connected = port
    return port


def send(dmsg, port):
    """This function is what is used to send the final message. It takes the port
    you want and the message as arguments."""
    port.write(dmsg)


def pack(channels):
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
    return message #list(map(lambda i :struct.pack(b'B',i),message))
def commands(channels):
    global connected
    """This function will take any amount of channels given and both pack and send
    the message to the flight controller. Values given must still be given in the
    order of the channels"""
    command = []
    for i in channels:
        command.append(i)
    command+=([1000]*(14-len(channels)))
    message = pack(command)
    print(message)
    # with connecttoport('/dev/ttyS0') as port:
    #     print (channels)
    #     send(message, port)
    # print(channels)
    # print(len(message))
    # print(max(message))
    if connected:
        print('first happened')
        send(message, connected)
    else:
        print('other option')
        send(message, connecttoport('/dev/ttyS0'))

def test():
    for i in range(4000):
        commands([1000]*4)
        sleep(0.007)
    # print("start")
    # port = serial.Serial('/dev/ttyS0',115200, timeout=10, write_timeout=10 )
    # port.write(struct.pack(b'B',128))
    # print("end")
    # port=connecttoport('/dev/ttyS0')
    # channel = [1000]*14
    # message = pack(channel)
    # print(message)
    # for i in range(2000):
    #     send(message, port)
    # #disarmed
    # for i in range(100):
    #     commands([1500, 1500, 1500, 885, 1500, 1500])
    #     sleep(1)
    #
    # #arm
    # for i in range(100):
    #     commands([1500, 1500, 1500, 885, 1500, 1900])
    #     sleep(1)
    #
    # #throttle to 1500
    # for i in range(100):
    #     commands([1500, 1500, 1500, 1500, 1500, 1900])
    #     sleep(1)
    #
    # #throttle to 885
    # for i in range(100):
    #     commands([1500, 1500, 1500, 885, 1500, 1900])
    #     sleep(1)
    #
    # #dissarm
    # for i in range(100):
    #     commands([1500, 1500, 1500, 885, 1500, 1500])
    #     sleep(1)

if __name__ == "__main__":
    test()
