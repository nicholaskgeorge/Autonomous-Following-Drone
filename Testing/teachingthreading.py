import threading
import time

def sametime():
    time.sleep(2)
    print('We did it')

simo = threading.Thread(target=sametime, args=())
simo.start()
print('We are starting')
time.sleep(4)
print('We ended')
