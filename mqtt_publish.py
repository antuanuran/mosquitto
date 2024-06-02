import sys

import paho.mqtt.client as paho # Создадим клиента-создателя через paho

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Connection established")
    sys.exit(-1)

client.publish("topic_mqtt", "Проверяем на отправку от клиента-создателя через локальную МОСКИТУ")

client.disconnect()
