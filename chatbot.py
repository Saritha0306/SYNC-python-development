import random

def chatbot():
    responses = {
        "hello": ["Hi there!", "Hello!", "Hi!"],
        "how are you": ["I'm doing well, thank you!", "I'm good, thanks for asking!"],
        "what's your name": ["My name is Chatbot!", "I'm Chatbot!"],
        "bye": ["Goodbye!", "Bye!"]
    }

    print("Hi! I'm a chatbot. What's your name?")
    name = input()
    print(f"Nice to meet you, {name}!")

    while True:
        user_input = input("Say something: ")
        if user_input.lower() == "bye":
            print(random.choice(responses["bye"]))
            break
        else:
            for key in responses:
                if key in user_input.lower():
                    print(random.choice(responses[key]))
                    break
                
chatbot()
