from django.http import JsonResponse
from django.shortcuts import render
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

#
# # Define a function to handle user input and generate a response
# def get_response(user_input):
# payload = {
#             "inputs": {
#                 "question": question,
#                 "context": context
#             }
#         }
#         response = requests.post(API_URL, headers=headers, json=payload)
#         answer = response.json()['answer']


#         tokenizer = AutoTokenizer.from_pretrained('squirro/albert-base-v2-squad_v2')
#         model = AutoModelForQuestionAnswering.from_pretrained('squirro/albert-base-v2-squad_v2')
#         inputs = tokenizer.encode_plus(user_input, context, add_special_tokens=True, return_tensors="pt")
#         input_ids = inputs["input_ids"].tolist()[0]
#         outputs = model(**inputs)
#         answer_start_scores = outputs.start_logits
#         answer_end_scores = outputs.end_logits
#         answer_start = torch.argmax(answer_start_scores)
#         answer_end = torch.argmax(answer_end_scores) + 1
#         response = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
#     return response
#
#
# # Define a function to handle the chatbot
# import speech_recognition as sr
# #
# #
# def chatbott(request):
#     if request.method == 'POST':
#         print("hello")
#         question = request.POST['question']
#         answer = get_response(question)
#         if not user_input:
#             # If user input is empty, try speech recognition
#             r = sr.Recognizer()
#             with sr.Microphone() as source:
#                 audio = r.listen(source)
#             try:
#                 user_input = r.recognize_google(audio)
#             except sr.UnknownValueError:
#                 pass
#             except sr.RequestError as e:
#                 return render(request, 'chatbot.html', {'response': str(e)})
#         print(answer)
#         response_data = {'question': question,'answer': answer}
#         return JsonResponse(response_data)


    # return render(request, 'chatbot.html', {'response': response})
#     else:
#         return render(request, 'guidance.html')
# from django.shortcuts import render


def answer_question(question, context):
    pages = ["category", "shop", "login", "register", "myprofile"]
    user_input = question.lower().strip()
    if user_input == "hi" or user_input == "hello" or user_input == "hlo":
        answer= "Hello! How can I assist you today?"
    elif user_input in pages:
        response="http://127.0.0.1:8000/{ user_input }"
        # answer= f'Sure, I can help you navigate to the {user_input} page. Here is the link: <a href="http://127.0.0.1:8000/{ user_input }" target="_blank">http://127.0.0.1:8000/{ user_input }</a>'
        answer= f'Sure, I can help you navigate to the {user_input} page. Here is the link: http://127.0.0.1:8000/{ user_input }'


    elif "help" in user_input:
        answer= "I can help you navigate to different pages on our website. Just tell me which page you'd like to visit, or type 'menu' to see a list of options."
    elif user_input == "menu":
        answer= "Here are some options:\ncategory\nshop\nlogin\nregister\nmyprofile"
    else:
        tokenizer = AutoTokenizer.from_pretrained('squirro/albert-base-v2-squad_v2')
        model = AutoModelForQuestionAnswering.from_pretrained('squirro/albert-base-v2-squad_v2')
        inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
        input_ids = inputs["input_ids"].tolist()[0]
        outputs = model(**inputs)
        answer_start_scores = outputs.start_logits
        answer_end_scores = outputs.end_logits
        answer_start = torch.argmax(answer_start_scores)
        answer_end = torch.argmax(answer_end_scores) + 1
        answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
    if answer == "[CLS]":
        answer = "sorry i cannot find the result. Can you specify with the context"

    return answer


def chatbot(request):
    print("working")
    if request.method == 'POST':
        question = request.POST['question']
        context = "Django is a powerful and widely used web framework written in Python that allows developers to build robust web applications quickly and efficiently. It follows the Model-View-Template (MVT) architecture, which promotes clean separation of concerns and encourages reusable code. Django provides a plethora a of built-in features and tools that simplify common web development tasks such as URL routing, authentication, database management, and form handling."
        answer = answer_question(question, context)
        print(question)
        print(answer)
        response_data = {'question': question, 'context': context, 'answer': answer}
        return JsonResponse(response_data)
    else:
        return render(request, 'chatbot.html')