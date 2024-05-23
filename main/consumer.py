import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.0.10',  # Update with container name/IP
                              port=5672,
                              credentials=pika.PlainCredentials(username='main', password='main'))  # Update credentials if needed
)

channel = connection.channel()

channel.queue_declare(queue='admin')

def consume(ch, method, properties, body):
    print( ' [x] Received %r' % body)

channel.basic_consume(queue='admin', on_message_callback=consume, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
