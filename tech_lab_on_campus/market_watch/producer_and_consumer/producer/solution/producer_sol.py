import pika
import os

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key, exchange_name):
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        setupRMQConnection(self)
    
    def setupRMQConnection(self):
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection(parameters=con_params)

    def publishOrder(self, message):
        channel = connection.channel()
        exchange = channel.exchange_declare(exchange="Exchange Name")

        channel.basic_publish(
            exchange= self.exchange_name,
            routing_key= self.routing_key,
            body="Message")

        channel.close()
        connection.close()