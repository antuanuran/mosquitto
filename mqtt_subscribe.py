import sys

import paho.mqtt.client as paho


def onMessage(client, userdata, message):
    print(message.payload.decode(), message.topic)


client = paho.Client()
client.on_message = onMessage


if client.connect("localhost", 1883, 60) != 0:
    print("Connection established")
    sys.exit(-1)

client.subscribe("test_mqtt")

try:
    print("Press Ctrl-C to quit....")
    client.loop_forever()
except KeyboardInterrupt:
    print("Disconnecting...")


client.disconnect()
