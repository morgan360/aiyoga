from django.shortcuts import render
from .forms import CreateAiForm
from django.http import HttpResponse
import requests
from .models import AiModel
import openai
import os
from django.conf import settings
import environ
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

API_KEY = getattr(settings, 'OPEN_API_KEY', None)
# env = environ.Env()
# environ.Env.read_env()
#
# openai.api_key = env('OPENAI_API_KEY')

openai.api_key = API_KEY


# Access a variable from the settings file

def home_page(request):
    return render(request, 'home.html')


# This works calls Yoga.html
@login_required
def ask_question(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        new_question = ' Yoga pose Sanskrit Name for: ' + question
        response1 = openai.Completion.create(
            engine="text-davinci-002",
            prompt=new_question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.01,
        )
        answer = response1["choices"][0]["text"]
        # save the prompt
        prompt = AiModel(prompt=question)
        prompt.save()
        # save the response
        reply = AiModel(response=answer)
        reply.save()
        answer = 'neckpain'
        # get the image based on the response
        response = openai.Image.create(
            prompt='Yoga pose For' + answer,
            n=1,
            size="256x256",
        )
        image_url = response['data'][0]['url']
        # save the image reference
        reply = AiModel(image_url=image_url)
        reply.save()
    else:
        answer = ''
        # prompt = ""
        image_url = ""

        return render(request, 'ai/yoga.html', {'answer': answer, 'image_url': image_url})
    context = {
        'question': new_question,
        'answer': answer,
        'image_url': image_url,

    }
    return render(request, 'ai/yoga.html', context)


@login_required
def create_ai_form(request):
    if request.method == 'POST':
        form = CreateAiForm(request.POST)
        if form.is_valid():
            session_name = form.cleaned_data['name']
            return HttpResponse('Session Created' + session_name)
    form = CreateAiForm({'name': 'Ai-Session x'})
    return render(request, 'ai/create_ai_form.html', {'form': form})
