import paho.mqtt.client as mqtt
import time

broker_address = "rule28.i4t.swin.edu.au"
username = "104315180"
password = "104315180"

client = mqtt.Client("Device1")
client.username_pw_set(username, password)
client.connect(broker_address)

private_topic = f"{username}/private/device1"

for i in range(1, 6):
    message = f"Data from Device 1, Message {i}"
    client.publish(private_topic, message)
    time.sleep(1)

client.loop_start()
