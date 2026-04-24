from fastapi import FastAPI
from backend.personas import personas
from backend.router import init_db, route_post
from backend.graph import build_graph
from pydantic import BaseModel

app = FastAPI()

graph = build_graph()
init_db(personas)

# ✅ Request model
class PostRequest(BaseModel):
    post: str

@app.post("/generate")
def generate(req: PostRequest):
    post = req.post

    bots = route_post(post)
    outputs = []

    for b in bots:
        res = graph.invoke({"persona": personas[b], "bot_id": b})
        outputs.append(res["output"])

    return {"bots": bots, "responses": outputs}


# from personas import personas
# from router import init_vector_db, route_post
# from graph import build_graph
# from rag import generate_defense
#
# init_vector_db(personas)
# app_graph = build_graph()
#
# post = "OpenAI replacing developers"
# bots = route_post(post)
#
# print("Matched Bots:", bots)
#
# for b in bots:
#     result = app_graph.invoke({
#         "persona": personas[b],
#         "bot_id": b
#     })
#     print(result)