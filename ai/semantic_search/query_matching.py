from typing import List, Dict

from sentence_transformers import SentenceTransformer, util
import numpy as np

current_question = ["Help me with Back Pain"]
saved_questions = [
    "I have a sore back",
    "help me with neck pain",
    "how can I get more flexible",
]


model = SentenceTransformer("sentence-transformers/paraphrase-distilroberta-base-v1")


def retrieve_most_similar_query(
    current_query: str, saved_queries: List[str]
) -> Dict[str, float]:
    embeddings = model.encode([current_query], convert_to_tensor=True)
    # in future save and store in DB
    embeddings_saved = model.encode(saved_queries, convert_to_tensor=True)
    cosine_scores = np.array(util.cos_sim(embeddings, embeddings_saved))
    closest_query_score = cosine_scores[np.argmax(cosine_scores)]
    closest_query = saved_queries[np.argmax(cosine_scores)]
    return {closest_query: np.float(closest_query_score)}
