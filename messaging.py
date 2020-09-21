import paho.mqtt.client as mqtt
import time
import threading
class Messages(threading.Thread):
    """This is the class holdign the functions which manage communication with the
       drone using the MQTT protocol. This will work over any network that both
       the drone and the computer are on together."""
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
        """Sets up connection to the broker to send or recive messages. In the
        case of the drone the Pi is the broker"""
        if rc == 0:
            print("Drone Connection Established")
        else:
            print("bad connection Returned code=",rc)
        self.client.subscribe(self.topic)
    def on_subscribe(self,client, userdata, mid, granted_qos):
        """Subscribes to a certian topic on which messages will be sent"""
        print("Subscription complete")
    def on_message(self,client,userdata,msg):
        """Saves any received message"""
        self.received = str(msg.payload.decode())
    def on_disconnect(self,client,userdata,flags,rc=0):
        """Ends conection with broker"""
        print('The connection has been closed')
    def end(self):
        """This function ends the loop which sends and recives messages"""
        time.sleep(1)
        print('Ending Connection')
        self.client.loop_stop()
        self.client.disconnect()
    def addsub(self,topic):
        """Function lets you subscribe to another topic if needed"""
        self.client.subscribe(topic)
    def send(self,msg,topic=None):
        """Sends message"""
        if topic is None:
            topic = self.topic
        self.client.publish(topic,msg)
    def run(self):
        """Makes thread which is used to constanly read and wait for messages"""
        print('Setting up connection and starting thread')
        self.client.connect(self.broker)
        self.client.loop_forever()

if __name__ == "__main__":
    message = Messages('Laptop',topic="test/message")
    message.begin()
    message.send("test/message",'Check')
    time.sleep(2)
    message.end()
