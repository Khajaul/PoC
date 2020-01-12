import pika

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='Tiroir')
channel.exchange_declare(exchange='Tiroir', exchange_type='direct')
channel.queue_bind(exchange='Tiroir', queue='Tiroir')
