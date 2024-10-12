import pika, json

params = pika.URLParameters('amqps://mwyaidcw:8kEi9Pa373iN9A-M6j0G4ypIhYw-fE7r@chimpanzee.rmq.cloudamqp.com/mwyaidcw')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method,body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='django',body = json.dumps(body),properties = properties)
    print("added to the django queue",body)