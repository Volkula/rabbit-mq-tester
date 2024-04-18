#!/usr/bin/env python
import pika
import sys
import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()

    username = os.getenv('RABBITMQ_USERNAME', 'rmq-user')
    password = os.getenv('RABBITMQ_PASSWORD', 'pwd')
    host = os.getenv('RABBITMQ_HOST', 'localhost')
    port = int(os.getenv('RABBITMQ_PORT', 5672))
    virtual_host = os.getenv('RABBITMQ_VIRTUAL_HOST', '/')

    return username, password, host, port, virtual_host

def send_message(message):
    username, password, host, port, virtual_host = load_config()

    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(host, port, virtual_host, credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent '{message}'")

    connection.close()

def receive_messages():
    # Load RabbitMQ connection details
    username, password, host, port, virtual_host = load_config()

    # Establish connection
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(host, port, virtual_host, credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declare queue
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # Subscribe to the queue to consume messages
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    try:
        # Start consuming messages
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted, closing connection...')
        # Stop consuming messages
        channel.stop_consuming()
        # Close the connection
        connection.close()
        print('Connection closed')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: script.py [-s/-r] [-m message]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == '-s':
        if len(sys.argv) < 4 or sys.argv[2] != '-m':
            print("Usage: script.py -s -m message")
            sys.exit(1)
        message = sys.argv[3]
        send_message(message)
    elif mode == '-r':
        receive_messages()
    else:
        print("Invalid mode. Use -s for sending or -r for receiving messages.")
        sys.exit(1)
