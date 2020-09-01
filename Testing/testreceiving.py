import paho.mqtt.client as mqtt
import time
def on_log(client,userdata,level,buf):
    print("log: "+buf)
def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("connected OK")
    else:
        print("bad connection Returned code=",rc)
    client.subscribe('test/message')
def on_message(client,userdata,msg):
    message=str(msg.payload.decode())
    print(message)
broker = "localhost"
client = mqtt.Client("Get")

client.on_connect = on_connect
client.on_message = on_message
#client.on_log = on_log
print("Connecting to broker ",broker)

client.connect(broker)
client.loop_forever()
client.publish("test/message",'I Can send too')
time.sleep(4)
