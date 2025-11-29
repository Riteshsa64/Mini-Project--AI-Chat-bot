# Rule Based AI Python ChatBot

import datetime
import time

name = input("Swagat h, enter your name : ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning, ", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon, ", name)
elif 17 <= presentHour <= 20:
    print("Good evening, ", name)
else:
    print("Good night, ", name)

print("Namaste! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")
# Chatbot Memory Creation (dictionary of responses)

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am running perfectly! How are you doing today?",
    "who are you": "I am smart AI chatbot created by Ritesh.",
    "tell me a joke": "Sure! Why don’t programmers like nature? Because it has too many bugs! 😄",
    "goodnight": "Sleep tight! The night is here to give you peace.",
    "thanks": "You are welcome! Let me know if you need anything else."
}



# Method/Function to get response of ChatBot

def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. Mai jald hi ye sikh lunga!"


# Take user input
userInput = input("Please ask your question: ")
reply = getResponseBot(userInput)
print(reply)