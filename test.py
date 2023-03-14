# import speech_recognition as sr
#
#
#
# from googletrans import Translator
#
#
# # from vaderSentiment.vaderSentiment import SentimentIntensityAnaly2zer
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#
#
# def takeCommand(p):
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#
#
#         print('Listening')
#         r.pause_threshold = 0.7
#         audio = r.listen(source)
#         try:
#             print("Recognizing")
#
#             Query = r.recognize_google(audio,language=p)#, language='hi-In'
#
#
#             print("the query is printed='", Query, "'")
#
#
#
#
#         except Exception as e:
#             print(e)
#             print("Say that again sir")
#             return "None"
#         return Query
#
# import time
#
# def trans(query):
#     translator = Translator()
#     time.sleep(1)
#     result = translator.translate(query, dest='en', src='auto')
#     return result
# def htr(query):
#
#     translator = Translator()
#     result = translator.translate(query,dest='hi', src='auto')
#     return result
#
#
# lang=int(input("choose the language\n1.Hindi\n2.Malayalam\n3.Marathi\n4.Kannada\n5.Gujarati"))
# if lang ==1:
#     p='hi-In'
# if lang==2:
#     p='ml-In'
# if lang==4:
#     p='kn-In'
# if lang==3:
#     p='mr-In'
# if lang==5:
#     p='gu-In'
#
#
# query=takeCommand(p)
#
#
# text=trans(query)
#
#
# t1=htr(query)
#
#
# print(text)
# print(t1)
#
# analyzer = SentimentIntensityAnalyzer()
#
#
# sentiment_dict = analyzer.polarity_scores(text.text)
#
# print("\nTranslated Sentence=", text,text, "\nDictionary=", sentiment_dict)
# if sentiment_dict['compound'] >= 0.05:
#     print("It is a Positive Sentence")
#
# elif sentiment_dict['compound'] <= - 0.05:
#     print("It is a Negative Sentence")
# else:
#     print("It is a Neutral Sentence")

import random

# Define a function to handle user input and generate a response
def get_response(user_input):
    pages = ["category", "shop", "login", "register", "myprofile"]
    user_input = user_input.lower().strip()
    if user_input == "hi" or user_input == "hello":
        return "Hello! How can I assist you today?"
    elif user_input in pages:
        return f"Sure, I can help you navigate to the {user_input} page. Here's the link: http://127.0.0.1:8000/{user_input}"
    elif "help" in user_input:
        return "I can help you navigate to different pages on our website. Just tell me which page you'd like to visit, or type 'menu' to see a list of options."
    elif user_input == "menu":
        return "Here are some options:\ncategory\nshop\nlogin\nregister\nmyprofile"
    else:
        return "I'm sorry, I didn't understand. Please try again or type 'help' for assistance."

# Define a function to start the chatbot
def start_chat():
    print("Welcome to our website! How can I assist you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == "bye":
            print("Goodbye!")
            break
        else:
            response = get_response(user_input)
            print(response)

# Start the chatbot
start_chat()

