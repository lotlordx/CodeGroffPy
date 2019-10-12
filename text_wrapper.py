import textwrap

rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """

INDENTS = 4


def print_hanging_indents(poem):
    pass


prefix = "  "
preferredWidth = 70

message = rosetti_unformatted


remove_indent = textwrap.dedent(rosetti_unformatted)
wrapper = textwrap.TextWrapper(subsequent_indent=' '*len(prefix))
print(wrapper.fill(remove_indent))


