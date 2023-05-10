import webbrowser
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.template.defaultfilters import safe
from products.models import House_Product
API_URL = "https://api-inference.huggingface.co/models/squirro/albert-base-v2-squad_v2"
headers = {"Authorization": "Bearer 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"}

def answer_question(question, context):
    pages = ["home","map","category", "shop", "login","logout", "register","myprofile"]
    user_input = question.lower().strip()
    if user_input == "hi" or user_input == "hello" or user_input == "hlo":
        answer= "Hello! How can I assist you today?"
    elif user_input in pages:
        link = f'http://127.0.0.1:8000/{user_input}'
        answer = f"Sure, I can help you navigate to the {user_input} page. <a href='{link}' style='color:red;'>Click Here</a>"
        webbrowser.open_new_tab(link)

    elif user_input == "help" or user_input == "hellp" or user_input == "hellp me" or user_input == "help me":
        answer= "I can help you navigate to different pages on our website. Just tell me which page you'd like to visit, or type 'menu' to see a list of options."
    elif user_input == "menu":
        answer= "Here are some options:\nhome,\nmap,\ncategory\n,shop\n,login,\nregister,\nlogout"
    else:

        payload = {
            "inputs": {
                "question": question,
                "context": context
            }
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        answer = response.json()['answer']
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
        # details += " user name is "+str(h_product.user.fname)
        details += " The advertisment title given by " + str(h_product.user.fname) +" is " + h_product.ad_title
        details += " Rupees " + str(h_product.rent) +" for a month "
        details += f" The location available  for advertisement given by {h_product.user.fname} is " + h_product.location+"," + h_product.city+"\n"
        h_product_list.append(product_details)
    if request.method == 'POST':
        question = request.POST['question']
        question_malayalam=question
        context=f'''
        {details}
        AnyRent is a comprehensive rental platform that offers users a range of products across four primary categories: houses and apartments, furniture, cars, and bikes.
        
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
        response_data = {'question': question_malayalam, 'context': context, 'answer': safe(answer)}
        return JsonResponse(response_data)
    else:
        return render(request, 'chatbot.html')


