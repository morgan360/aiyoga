import random
from typing import List

import pandas as pd

from ai.prompt_engineering import open_ai_request, config


def run_open_ai_requests(list_of_questions: List[str]) -> pd.DataFrame:
    """
    This function takes a list of questions and returns a list of AI generated Yoga Sequences and saves to csv.
    """
    df = pd.DataFrame(
        columns=["question", "skill_level", "duration" "prompt", "answer", "image_url"]
    )
    for question in list_of_questions:
        skill_level = random.sample(config.PROMPT_SKILL_LEVELS, 1)[0]
        duration = random.sample(config.PROMPT_DURATIONS, 1)[0]
        response = open_ai_request.prompt_gpt3(skill_level, duration, question)
        df = df.append(response, ignore_index=True)

    # calculate current timestamp
    timestamp = pd.Timestamp.now()
    df.to_csv(f"ai/prompt_engineering/ai_generated_yoga_sequences{timestamp}.csv")
