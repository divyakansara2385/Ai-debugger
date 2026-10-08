import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_error_patterns():
    with open("data/error_patterns.json", "r", encoding="utf-8") as file:
        return json.load(file)


def find_similar_error(error):
    patterns = load_error_patterns()

    error_text = (
        f"{error['type']} "
        f"{error.get('variable', '')} "
        f"is used but may not be defined"
    )

    pattern_texts = [
        pattern["description"]
        for pattern in patterns
    ]

    vectorizer = TfidfVectorizer()

    all_texts = [error_text] + pattern_texts

    tfidf_matrix = vectorizer.fit_transform(all_texts)

    similarities = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )[0]

    best_index = similarities.argmax()

    return {
        "pattern": patterns[best_index],
        "similarity": similarities[best_index]
    }


def explain_error(error):

    result = find_similar_error(error)

    pattern = result["pattern"]

    return {
        "explanation": pattern["explanation"],
        "suggested_fix": pattern["fix"],
        "similarity": result["similarity"]
    }