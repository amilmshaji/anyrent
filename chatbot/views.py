from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import random

# Define a function to handle user input and generate a response
def get_response(user_input):
    pages = ["category", "shop", "login", "register", "myprofile"]
    user_input = user_input.lower().strip()
    if user_input == "hi" or user_input == "hello":
        return "Hello! How can I assist you today?"
    elif user_input in pages:
        return f'Sure, I can help you navigate to the {user_input} page. Here is the link: <a href="http://127.0.0.1:8000/{ user_input }" target="_blank">http://127.0.0.1:8000/{ user_input }</a>'

    elif "help" in user_input:
        return "I can help you navigate to different pages on our website. Just tell me which page you'd like to visit, or type 'menu' to see a list of options."
    elif user_input == "menu":
        return "Here are some options:\ncategory\nshop\nlogin\nregister\nmyprofile"
    else:
        return "I'm sorry, I didn't understand. Please try again or type 'help' for assistance."

# Define a function to handle the chatbot
import speech_recognition as sr


def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        if not user_input:
            # If user input is empty, try speech recognition
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                user_input = r.recognize_google(audio)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                return render(request, 'chatbot.html', {'response': str(e)})
        response = get_response(user_input)
        return render(request, 'chatbot.html', {'response': response})
    else:
        return render(request, 'chatbot.html')

