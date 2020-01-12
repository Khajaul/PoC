import pika
import sys
from datetime import datetime
import time

date = datetime.now()
date =time.mktime(date.timetuple())

drawer = sys.argv[1]
masse = sys.argv[2]
print(masse)

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))
channel = connection.channel()


channel.basic_publish(exchange='Tiroir',
                      routing_key='',
                      body='{"DATE": "%s", "ID_Client": "Client1", "ID_Drawer": "Drawer%s", "VALUE": "%s"}'%(date,drawer,masse))

print('{"DATE": "%s", "ID_Client": "Client1", "ID_Drawer": "Drawer%s", "VALUE": "%s"}'%(date,drawer,masse))
