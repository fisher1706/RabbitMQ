import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
print("[*] Waiting for messages. To exit press CTRL+C")

queue = 'hello'

def callback(ch, method, properties, body):
    print("[x] Received %r" % (body,))

channel.basic_consume(queue=queue, on_message_callback=callback)
channel.start_consuming()
