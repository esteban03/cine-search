import numpy as np
from sentence_transformers import SentenceTransformer, util
from data import tarantino_movies

def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings_movies = model.encode(
        [
            "Title: {title}; Year: {year}; Synopsis: {synopsis}; Notes: {notes};".format(**movie)
            for movie in tarantino_movies
        ],
        normalize_embeddings=True,
    )

    query = input("Describe your favorite Tarantino movie: ")
    embeddings_query = model.encode(query, normalize_embeddings=True)

    scores = util.dot_score(embeddings_query, embeddings_movies)[0].cpu().numpy()
    idx_max = np.argmax(scores)

    best_result = tarantino_movies[idx_max]
    print("Best result: ", best_result["title"])
    print("Score: ", scores[idx_max])

if __name__ == "__main__":
    main()