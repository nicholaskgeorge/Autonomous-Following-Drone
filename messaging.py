import paho.mqtt.client as mqtt
import time
import threading
class Messages(threading.Thread):
    def __init__(self,clientname,broker="10.49.12.253",topic = "test/message"):
        super().__init__()
        self.broker = broker
        self.topic = topic
        self.clientname = clientname
        self.client = mqtt.Client(self.clientname)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_subscibe = self.on_subscribe
        self.received = ''
    def on_connect(self,client,userdata,flags,rc):
        if rc == 0:
            print("Drone Connection Established")
        else:
            print("bad connection Returned code=",rc)
        self.client.subscribe(topic)
    def on_subscribe(self,client, userdata, mid, granted_qos):
        print("Subscription complete")
    def on_message(self,client,userdata,msg):
        print('got a message')
        self.received = str(msg.payload.decode())
    def on_disconnect(self,client,userdata,flags,rc=0):
        print('The connection has been closed')
    def begin(self):
        print('Setting up connection')
        self.client.connect(self.broker)
        self.client.loop_forever()
    def end(self):
        time.sleep(1)
        print('Ending Connection')
        self.client.loop_stop()
        self.client.disconnect()
    def changesub(self,topic=None):
        if topic is None:
            topic = self.topic
        self.client.subscribe(topic)
    def send(self,msg,topic=None):
        if topic is None:
            topic = self.topic
        self.client.publish(topic,msg)
    def run(self):
        print('Setting up connection and starting thread')
        self.client.connect("10.49.12.253")
        self.client.loop_forever()
        time.sleep(1)

if __name__ == "__main__":
    message = Messages('Laptop',topic="test/message")
    message.begin()
    message.send("test/message",'Check')
    time.sleep(2)
    message.end()
