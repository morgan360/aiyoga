from django.shortcuts import render
from .forms import CreateAiForm
from django.http import HttpResponse
import requests
from .models import AiModel
import openai
import json
import re

openai.api_key = "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"


def home_page(request):
    return render(request, 'home.html')


# This works calls Yoga.html
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

        # get the image based on the response
        response = openai.Image.create(
            prompt='Black and white illustration for:' + answer,
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

        return render(request, 'yoga.html', {'answer': answer, 'image_url': image_url})
    context = {
        'question': new_question,
        'answer': answer,
        'image_url': image_url,

    }
    return render(request, 'yoga.html', context)


def generate_image(request):
    if request.method == 'POST':
        result = request.POST['prompt']
        prompt = AiModel(prompt=result)
        prompt.save()

        response = openai.Image.create(
            prompt=result,
            n=1,
            size="512x512",
        )
        image_url = response['data'][0]['url']
        img_save = AiModel(image_url=image_url)
        img_save.save()
    else:
        prompt = ""
        image_url = ""
        result = ''
    context = {
        'prompt': prompt,
        'result': result,
        'image_url': image_url
    }
    return render(request, 'image.html', context)


# ChatGPT
def tai_yoga(request):
    API_KEY = "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"
    prompt = "Can you please create a minimum of 6 different yoga poses  for a 60 minute yoga session."

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    text = response["choices"][0]["text"]
    # text =
    context = {
        'my_variable': 42,
        'response': response,
        'text': text,
    }
    return render(request, 'tai_yoga.html', context)


def create_ai_form(request):
    if request.method == 'POST':
        form = CreateAiForm(request.POST)
        if form.is_valid():
            session_name = form.cleaned_data['name']
            return HttpResponse('Session Created' + session_name)
    form = CreateAiForm({'name': 'Ai-Session x'})
    return render(request, 'create_ai_form.html', {'form': form})
