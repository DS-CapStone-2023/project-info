import os
import pulsar
import time
import random
import string
import logging
import sys


class Producer(object):
    """
    Create a pulsar producer that writes random messages to a topic
    """
    def __init__(self):
        self.token = os.getenv("ASTRA_STREAMING_TOKEN")
        self.service_url = os.getenv("ASTRA_STREAMING_URL")
        self.topic = os.getenv("ASTRA_TOPIC")
        self.client = pulsar.Client(self.service_url,
                                    authentication=pulsar.AuthenticationToken(self.token))
        self.producer = self.client.create_producer(self.topic)

    def produce_messages(self):
        """
        Create and send random messages
        """
        while True:
            # create a random string of varying length (length max = 1000)
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(3, 1000)))
            self.producer.send(random_string.encode('utf-8'))
            logging.info("Just wrote: {}".format(random_string))
            time.sleep(1)


def produce_messages():
    """
    Create an instance of the producer and fire it up to send messages until the program is terminated
    """
    producer = Producer()
    producer.produce_messages()
    producer.client.close()


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout,
                        level=logging.INFO)
    produce_messages()
