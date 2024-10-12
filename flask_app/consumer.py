import pika, json
from app import Meal,db, app
params = pika.URLParameters('amqps://mwyaidcw:8kEi9Pa373iN9A-M6j0G4ypIhYw-fE7r@chimpanzee.rmq.cloudamqp.com/mwyaidcw')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='django')

def callback(ch,method,properties,body):
    print("flask is receiving")
    data = json.loads(body)
    print(type(data))
    print(data)
    with app.app_context():
        meal = Meal(id= data['id'], name= data['name'], category= data['category'], area= data['area'],image=data['image'])
        # print(meal)
        db.session.add(meal)
        db.session.commit()
        print('created in flaskdb')

channel.basic_consume(queue='django',on_message_callback=callback,auto_ack=True)
print('Consuming started')
channel.start_consuming()
channel.close()