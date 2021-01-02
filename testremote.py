from messaging import Messages
from time import sleep
import keyboard
message = Messages('Laptop',topic="test/message", broker ="192.168.1.11")
message.start()
while True:
    sleep(0.08)
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('p'):  # if key 'q' is pressed
            message.send('disarm')
        if keyboard.is_pressed('o'):  # if key 'q' is pressed
            message.send('arm')
        if keyboard.is_pressed('u'):  # if key 'q' is pressed
            message.send('up')
        elif keyboard.is_pressed('i'):
            message.send('down')
        elif keyboard.is_pressed('w'):
            message.send('forward')
        elif keyboard.is_pressed('s'):
            message.send('backward')
        elif keyboard.is_pressed('a'):
            message.send('left')
        elif keyboard.is_pressed('d'):
            message.send('right')
        elif keyboard.is_pressed('q'):
            message.send('yawleft')
        elif keyboard.is_pressed('e'):
            message.send('yawright')
        elif keyboard.is_pressed('`'):
            message.send('land')
        elif keyboard.is_pressed('0'):
            message.send('stop')

        # This is constantly sent when no buttons are pressed. It is a way for The
        # drone to know that we still have communication with the computer. If the
        # drone does not recive a message of some kind within a certian time period
        # it will automatially descend and land.

        else:
            message.send('stable')
    except:
        pass
