import openai
from django.conf import settings
from ai.prompt_engineering import config

API_KEY = getattr(settings, "OPEN_API_KEY", None)


openai.api_key = API_KEY


def prompt_gpt3(skill_level: str, duration: int, question: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=config.PROMPT.format(skill_level, duration, question),
        temperature=0.7,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[],
    )
    answer = response["choices"][0]["text"]
    # save the prompt
    # save the response
    # get the image based on the response
    response = openai.Image.create(prompt=answer, n=1, size="256x256")
    image_url = response["data"][0]["url"]
    # save the image reference
    return {
        "question": question,
        "skill_level": skill_level,
        "duration": duration,
        "prompt": config.PROMPT.format(skill_level, duration, question),
        "answer": answer,
        "image_url": image_url,
    }
