import paho.mqtt.client as mqtt
import time
class Messages():
    def __init__(self,broker="10.49.12.253"):
        self.broker = broker
        self.client = mqtt.Client("Laptop")
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.received = ''
    def on_connect(self,client,userdata,flags,rc):
        if rc == 0:
            print("Drone Connection Established")
        else:
            print("bad connection Returned code=",rc)
    def on_message(client,userdata,msg):
        message=str(msg.payload.decode("utf-8","ignore"))
        self.received = message
    def on_disconnect(self,client,userdata,flags,rc):
        print('The connection has been closed')
    def begin(self):
        print('Setting up connection')
        self.client.connect("10.49.12.253")
        self.client.loop_start()
        time.sleep(1)
    def end(self):
        time.sleep(1)
        print('Ending Connection')
        self.client.loop_stop()
        self.client.disconnect()
    def startsub(self,topic):
        self.client.subscribe(topic)
    def send(self,topic, msg):
        self.client.publish(topic,msg)

if __name__ == "__main__":
    message = Messages()
    message.begin()
    message.send("test/message",'Check')
    message.end()