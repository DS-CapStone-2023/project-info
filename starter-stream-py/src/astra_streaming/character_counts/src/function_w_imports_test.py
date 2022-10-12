from pulsar import Function
from character_count import character_count


class CounterFunction(Function):
    def __init__(self):
        self.output_topic = 'persistent://twitter-test/default/counter-test-topic'

    def process(self, input, context):
        try:
            total_characters = character_count(input)
            context.publish(self.output_topic, "IMPORT TEST SUCCESS! Total characters: {}".format(str(total_characters)))

        except:
            warning = "Negaaahtive Ghostrider. {}".format(input)
            context.get_logger().warn(warning)
