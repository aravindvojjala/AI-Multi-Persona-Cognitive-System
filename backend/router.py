from sentence_transformers import SentenceTransformer
from backend.db import collection
import numpy as np
model = SentenceTransformer("all-MiniLM-L6-v2")


def init_db(personas):
    for bot_id, text in personas.items():
        emb = model.encode(text).tolist()
        collection.add(ids=[bot_id], embeddings=[emb], documents=[text])

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def route_post(post):
    post_emb = model.encode(post)

    data = collection.get(include=["embeddings"])

    scores = []

    for i in range(len(data["ids"])):
        bot_id = data["ids"][i]
        bot_emb = data["embeddings"][i]

        sim = cosine_similarity(post_emb, bot_emb)

        print("DEBUG:", bot_id, "Similarity:", sim)

        scores.append((bot_id, sim))   # ✅ collect scores

    # ✅ sort by similarity (highest first)
    scores.sort(key=lambda x: x[1], reverse=True)

    # ✅ pick top 1 (you can change to top 2 later)
    selected = [scores[0][0]]

    return selected

#-------------------------------------------------------------
# def route_post(post, threshold=0.3):
#     post_emb = model.encode(post)
#
#     data = collection.get(include=["embeddings"])
#
#     bots = []
#
#     for i in range(len(data["ids"])):
#         bot_id = data["ids"][i]
#         bot_emb = data["embeddings"][i]
#
#         sim = cosine_similarity(post_emb, bot_emb)
#
#         print("DEBUG:", bot_id, "Similarity:", sim)
#
#         if sim > 0:
#             bots.append(bot_id)
#
#     return bots
#------------------------------------------------------------------

#------------------------------------------------------------------
# def route_post(post, threshold=0.5):
#     emb = model.encode(post).tolist()
#     res = collection.query(query_embeddings=[emb], n_results=3)
#
#     bots = []
#     for i, dist in enumerate(res['distances'][0]):
#         sim = 1 - dist
#         print("DEBUG:", res['ids'][0][i], "Similarity:", sim)
#
#         if sim > threshold:
#             bots.append(res['ids'][0][i])
#     return bots
#-------------------------------------------------------------------------

# from sentence_transformers import SentenceTransformer
# import chromadb
#
# model = SentenceTransformer('all-MiniLM-L6-v2')
# client = chromadb.Client()
# collection = client.create_collection("bots")
#
#
# def init_vector_db(personas):
#     for bot_id, text in personas.items():
#         emb = model.encode(text).tolist()
#         collection.add(ids=[bot_id], embeddings=[emb], documents=[text])
#
#
# def route_post(post, threshold=0.75):
#     emb = model.encode(post).tolist()
#     results = collection.query(query_embeddings=[emb], n_results=3)
#
#     matched = []
#     for i, dist in enumerate(results['distances'][0]):
#         similarity = 1 - dist
#         if similarity > threshold:
#             matched.append(results['ids'][0][i])
#     return matched