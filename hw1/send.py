#!/usr/bin/env python
import pika
import time
import random

conn_params = pika.ConnectionParameters('localhost', 5680)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue')

while(1):
    number = random.randint(-100, 100)
    channel.basic_publish(exchange='',
			  routing_key='first-queue',
			  body=str(number))
    print("Number", number, " sent")
    time.sleep(random.random() * 2)

connection.close()
