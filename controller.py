import paho.mqtt.client as mqtt

def on_log(client,userdata,level,buf):
    print("log: "+buf)
def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("Drone Connection Established")
    else:
        print("bad connection Returned code=",rc)
broker = "10.49.12.253"
client = mqtt.Client("Laptop")

client.on_connect = on_connect
#client.on_log = on_log

client.connect(broker)
client.loop_start()
