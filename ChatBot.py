import nltk
from nltk.chat.util import Chat, reflections


BOB_responses = [
    (r"Hi|Hello|Hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"What is your name?", ["You can call me BoB.", "I am Bot."]),
    (r"How are you?", ["I'm doing well, thank you!", "I'm fine, thanks for asking."]),
    (r"What is your favorite color?", ["I don't have a favorite color. As I'm just a program."]),
    (r"Who Programmed you?", ["I was build by Mr. Srujan Sane"]),
    (r"Bye|Goodbye", ["Goodbye", "See you later!", "Take care!"]),
   
]
BOB = Chat(BOB_responses, reflections)

def run_chatbot():
    print("Chat_Bot: Hi! I'm BoB, your friendly chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chat_Bot: Goodbye!")
            break
        response = BOB.respond(user_input)
        print("Chat_Bot:", response)

if __name__ == "__main__":
    nltk.download("punkt")
    run_chatbot()
