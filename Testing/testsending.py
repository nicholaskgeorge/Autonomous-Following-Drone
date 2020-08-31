# MQTT Publish Demo
#Publish two messages, to two different topics
import paho.mqtt.client as mqtt
import time
def on_log(client,userdata,level,buf):
    print("log: "+buf)
def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("connected OK")
    else:
        print("bad connection Returned code=",rc)
def on_message(client,userdata,msg):
    message=str(msg.payload.decode())
    print(message)
broker = "10.49.12.253"
client = mqtt.Client("Give")

client.on_connect = on_connect
client.on_message = on_message
#client.on_log = on_log
print("Connecting to broker ",broker)

client.connect(broker)
client.loop_start()
#client.subscribe('test/message')
client.publish("test/message",'IT WORKED!!!!')
time.sleep(4)
client.loop_stop()
# client.disconnect()
