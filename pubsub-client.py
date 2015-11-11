import json
import time
import paho.mqtt.client as mqtt

def on_connect(client, data, rc):
    print "Connected with result code {}".format(str(rc))
    # client.subscribe("$SYS/brokers/emqttd@127.0.0.1/uptime")
    client.subscribe("/demo/updates")

def on_message(client, data, message):
    print """
        Topic: {}
        Payload: {}
    """.format(message.topic, message.payload)

    time.sleep(1)
    client.publish("demo/updates", payload=message.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
