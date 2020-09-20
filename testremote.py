from messaging import Messages
from time import sleep
import keyboard
message = Messages('Laptop',topic="test/message")
message.start()
while True:
    sleep(0.08)
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('w'):  # if key 'q' is pressed
            message.send('up')
        elif keyboard.is_pressed('s'):
            message.send('down')
        else:
            message.send('stable')
            delay(0.5)
    except:
        pass
