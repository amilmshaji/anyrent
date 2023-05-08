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
from products.models import House_Product

tokenizer = AutoTokenizer.from_pretrained('squirro/albert-base-v2-squad_v2')
model = AutoModelForQuestionAnswering.from_pretrained('squirro/albert-base-v2-squad_v2')

def answer_question(question, context):
    pages = ["category", "shop", "login", "register", "myprofile"]
    user_input = question.lower().strip()
    if user_input == "hi" or user_input == "hello" or user_input == "hlo":
        answer= "Hello! How can I assist you today?"
    elif user_input in pages:
        response="http://127.0.0.1:8000/{ user_input }"
        print(user_input)
        answer= f'Sure, I can help you navigate to the {user_input} page. Here is the link: http://127.0.0.1:8000/{ user_input }'


    elif user_input == "help" or user_input == "hellp":
        answer= "I can help you navigate to different pages on our website. Just tell me which page you'd like to visit, or type 'menu' to see a list of options."
    elif user_input == "menu":
        answer= "Here are some options:\ncategory\nshop\nlogin\nregister\nmyprofile"
    else:

        inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
        input_ids = inputs["input_ids"].tolist()[0]
        outputs = model(**inputs)
        answer_start_scores = outputs.start_logits
        answer_end_scores = outputs.end_logits
        answer_start = torch.argmax(answer_start_scores)
        answer_end = torch.argmax(answer_end_scores) + 1
        answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
        print("helloooooooooooo")
    print(answer)
    if answer == "[CLS]" or answer =='':
        answer = "sorry i cannot find the result. Can you specify with the context"

    return answer


from googletrans import Translator
translator = Translator()

def chatbot(request):
    h_product_list = []
    details = "details of the products added"

    for h_product in House_Product.objects.all():
        product_details = {
            "id": h_product.id,
            "user_id": h_product.user_id,
            "ad_title": h_product.ad_title,
            "slug": h_product.slug,
            "add_info": h_product.add_info,
            "rent": h_product.rent,
            "bedroom": h_product.bedroom,
            "bathroom": h_product.bathroom,
            "builtup": h_product.builtup,
            "capacity": h_product.capacity,
            "type": h_product.type,
            "furnish": h_product.furnish,
            "location": h_product.location,
            "city": h_product.city,
            "state": h_product.state
        }
        details += " user name is "+str(h_product.user.fname)
        details += " the advertisment title " + str(h_product.rent) +" gave is " + h_product.ad_title
        details += " Rupees " + str(h_product.rent) +" for a month "
        details += f" The location for house {h_product.user.fname} gave  available is " + h_product.location+"," + h_product.city+" "
        h_product_list.append(product_details)
        print(details)
    if request.method == 'POST':
        question = request.POST['question']
        question_malayalam=question
        context=f'''AnyRent is a comprehensive rental platform that offers users a range of products across four primary categories: houses and apartments, furniture, cars, and bikes.
        
 

{details}
'''
        # Detect language of the question
        lang = translator.detect(question).lang

        # Translate Malayalam to English
        if lang == 'ml':
            question = translator.translate(question, src='ml', dest='en').text
            print("malayalam;;",question)

        # Get answer to question
        answer = answer_question(question, context)
        print(answer)

        # Translate answer to Malayalam if necessary
        if lang == 'ml':
            answer = translator.translate(answer, src='en', dest='ml').text
            print("malayalam",answer)

        # Return JSON response
        response_data = {'question': question_malayalam, 'context': context, 'answer': answer}
        return JsonResponse(response_data)
    else:
        return render(request, 'chatbot.html')


