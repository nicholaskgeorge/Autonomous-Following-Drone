import paho.mqtt.client as mqtt
import time
def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("connected OK")
    else:
        print("bad connection Returned code=",rc)
    client.subscribe('test/message')
def on_subscribe(client, userdata, mid, granted_qos):
    print('Subscription applied')
def on_message(client,userdata,msg):
    message=str(msg.payload.decode())
    print(message)
broker = "10.49.12.253"
client = mqtt.Client("Get")
client.on_subscribe = on_subscribe
client.on_connect = on_connect
client.on_message = on_message
print("Connecting to broker ",broker)
client.connect(broker)
client.loop_forever()
