import paho.mqtt.client as mqtt
import time

broker_address = "rule28.i4t.swin.edu.au"
port = 1883
username = "104315180"
password = "104315180"

client = mqtt.Client("PublisherDevice")

client.username_pw_set(username, password)

client.connect(broker_address, port=port, keepalive=60)

private_topic = f"{username}/private"
public_topic = "public"

for i in range(5):
    message = f"Message {i}"
    client.publish(private_topic, message)
    client.publish(public_topic, message)
    time.sleep(1)

client.disconnect()