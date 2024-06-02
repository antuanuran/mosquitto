import sys

import paho.mqtt.client as paho

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Connection established")
    sys.exit(-1)

client.publish("test_mqtt", "Проверяем на отправку")

client.disconnect()
