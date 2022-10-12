from pulsar import Function


class CounterFunction(Function):
    def __init__(self):
        self.output_topic = 'persistent://twitter-test/default/counter-test-topic'

    def process(self, input, context):
        try:
            total_characters = len(str(input).strip())
            context.publish(self.output_topic, "Total characters: {}".format(str(total_characters)))

        except:
            warning = "Negaaahtive Ghostrider. {}".format(input)
            context.get_logger().warn(warning)
