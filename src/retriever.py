from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def retrieve_relevant(query_embedding, memories, top_k=3):

    scores = []

    for item in memories:

        memory = item["memory"]

        similarity = cosine_similarity(
            [query_embedding],
            [memory.embedding]
        )[0][0]

        final_score = similarity * memory.strength

        scores.append((memory.content, final_score))

    ranked = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]
