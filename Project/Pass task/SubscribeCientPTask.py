import paho.mqtt.client as mqtt

broker_address = "rule28.i4t.swin.edu.au"
username = "104315180"
password = "104315180"

client = mqtt.Client("Device2")
client.username_pw_set(username, password)

private_topic = f"{username}/private/device1"
public_topic = "public"

def on_message(client, userdata, message):
    print(f"Received message on topic '{message.topic}': {message.payload.decode()}")

client.on_message = on_message

client.connect(broker_address)
client.subscribe([(private_topic, 0), (public_topic, 0)])

client.loop_forever()
