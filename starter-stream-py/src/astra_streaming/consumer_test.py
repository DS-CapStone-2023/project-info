import pulsar
import time
import os
import logging
import sys


class Consumer(object):
    """
    Create a pulsar producer that writes random messages to a topic
    """
    def __init__(self):
        self.token = os.getenv("ASTRA_STREAMING_TOKEN")
        self.service_url = os.getenv("ASTRA_STREAMING_URL")
        self.subscription =  os.getenv("ASTRA_TOPIC")
        self.client = pulsar.Client(self.service_url,
                                    authentication=pulsar.AuthenticationToken(self.token))
        self.consumer = self.client.subscribe(self.subscription, 'my-subscription')

    def read_messages(self):
        """
        Create and send random messages
        """
        while True:
            try:
                msg = self.consumer.receive(2000)
                logging.info("Horray! '{}' id='{}'".format(msg.data(), msg.message_id()))
                # Acknowledging the message to remove from message backlog
                self.consumer.acknowledge(msg)

            except:
                logging.info("Still waiting for a message...");
            time.sleep(1)


def read_messages():
    """
    Create an instance of the consumer and
    Fire it up to read messages until the program is terminated
    """
    consumer = Consumer()
    consumer.read_messages()
    consumer.client.close()


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout,
                        level=logging.INFO)
    read_messages()
