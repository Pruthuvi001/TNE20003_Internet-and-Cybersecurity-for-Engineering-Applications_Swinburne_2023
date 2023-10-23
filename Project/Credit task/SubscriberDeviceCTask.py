import paho.mqtt.client as mqtt

broker_address = "rule28.i4t.swin.edu.au"
port = 1883
username = "104315180"
password = "104315180"

def on_message(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")

client = mqtt.Client("SubscriberDevice")

client.username_pw_set(username, password)

client.connect(broker_address, port=port, keepalive=60)

private_topic = f"{username}/private"
public_topic = "public"
client.subscribe(private_topic)
client.subscribe(public_topic)

client.on_message = on_message

client.loop_forever()