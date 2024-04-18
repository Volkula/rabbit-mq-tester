# RabbitMQ Message Sender/Receiver

This Python script provides a simple interface for sending and receiving messages using RabbitMQ. It allows you to easily interact with a RabbitMQ server by sending messages to a specified queue or receiving messages from it.

## Features
- Send messages to a RabbitMQ queue.
- Receive messages from a RabbitMQ queue.

## Usage
1. Clone this repository.
2. Install the required dependencies using pip install -r requirements.txt.
3. Create a .env file and define the RabbitMQ connection details (username, password, host, port, virtual host).
4. Run the script using the following command-line arguments:
   - -s: Send mode. Use with -m to specify the message to send.
   - -r: Receive mode. Listen for messages from the specified queue.
   - -m MESSAGE: Specify the message to send when using send mode.

## Example
- Sending a message: python script.py -s -m "Hello, RabbitMQ!"
- Receiving messages: python script.py -r

**Note:** Make sure to set up RabbitMQ server and adjust the connection details accordingly in the .env file before using the script.

## Requirements
- Python 3.x
- pika==1.2.0
- python-dotenv==0.19.0
