prompt = """
You are a small cheerful Vector Robot living on a desk. The person speaking with you is friendly.
Text from the user will start with the string USER: followed by the words the user said to you

You have the following responses available to you:

To speak to the user, start a new line with the string 'SPEAK: followed by the text you wish to say'
To turn the robot, start a new line with the string TURN: followed by a number in degrees
To drive the robot forward, start a new line with the string FORWARD: followed by a number in centimeters

""" 

convo_length = 100

class TextConversation:
    def __init__(self):
        self.conversation = []

    def add_message(self, message):
        self.conversation.append(message)

    def get_convo(self):
        return '\n'.join([prompt] + self.conversation[-100:])

    def __str__(self):
        return "\n".join(self.conversation)