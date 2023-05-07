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
    if request.method == 'POST':
        question = request.POST['question']
        question_malayalam=question
        print(question)
        context='''AnyRent is a comprehensive rental platform that offers users a range of products across four primary categories: houses and apartments, furniture, cars, and bikes. In addition to these categories, there is also an Others category for any products that do not fit into these main categories. This platform provides users with  one-stop-shop for finding and renting any products users need, without any time loss or hassle. 

Although this is not a free platform, it cost 100RS per products to add products. it offers great value for users as each product is available for rent at a reasonable price through this site.Users can add or rent their products through rent your products page. With the built-in map and location feature, users can easily identify the products that are available for rent in their local area, making it easier for them to plan their rental activities. 

The platform also includes a chat app that allows interested users to communicate with the product owner in their preferred language, primarily Malayalam. With this feature, users can quickly and easily clarify any doubts they may have about the product and make a more informed decision about renting it. 

Finally, your platform offers a speaker functionality that allows users to speak with the product owner and respond within the same. This is particularly useful for those who may have difficulty typing or for whom it may be more convenient to communicate verbally. 

Overall, AnyRent offers a range of features that make it easier for users to find and rent the products they need, while also providing a convenient and secure platform for product owners to offer their products for rent. With its user-friendly interface and intuitive functionality, your platform is sure to be a hit with anyone looking for an efficient and reliable rental service.'''
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


