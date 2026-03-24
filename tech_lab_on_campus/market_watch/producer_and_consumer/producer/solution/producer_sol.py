import pika
import os
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key, exchange_name):
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()
    
    def setupRMQConnection(self):
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

    def publishOrder(self, message):
        self.channel = self.connection.channel()
        exchange = self.channel.exchange_declare(exchange=self.exchange_name)

        self.channel.basic_publish(
            exchange= self.exchange_name,
            routing_key= self.routing_key,
            body=message)

        self.channel.close()
        self.connection.close()