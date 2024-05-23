import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.0.10',  # Update with container name/IP
                              port=5672,
                              credentials=pika.PlainCredentials(username='main', password='main'))  # Update credentials if needed
)

channel = connection.channel()

channel.queue_declare(queue='admin')

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='Hello World!')
