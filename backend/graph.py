from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from typing import TypedDict

class GraphState(TypedDict, total=False):
    persona: str
    bot_id: str
    topic: str
    context: str
    output: str

load_dotenv(dotenv_path="C:/Users/Admin/AI_Cognitive_System/.env")

#print("API KEY:", os.getenv("CEREBRAS_API_KEY"))

llm = ChatOpenAI(
    api_key=os.getenv("CEREBRAS_API_KEY"),
    base_url="https://api.cerebras.ai/v1",
    model="llama3.1-8b"
)



# Dynamic decision node (REAL intelligence)
def decide_node(state):
    prompt = f"""
    Persona: {state['persona']}
    Decide a TRENDING topic based on personality.
    Output ONLY topic.
    """
    return {"topic": llm.invoke(prompt).content}

# Tool usage node

def search_node(state):
    topic = state['topic']

    # Replace with real API later
    if "AI" in topic:
        ctx = "Latest: GPT models replacing developers"
    elif "crypto" in topic:
        ctx = "Bitcoin ETF boom"
    else:
        ctx = "Global economy shifts"

    return {"context": ctx}

# Structured output node

def generate_node(state:GraphState):
    persona = state.get("persona")
    bot_id = state.get("bot_id")

    if not persona:
        raise ValueError("Persona missing in state")

    prompt = f"""
        You are this persona:
        {persona}

        Context: {state.get('context', '')}

        Generate a response.
        """

    response = llm.invoke(prompt)

    return {
        "output": response.content
    }

    # prompt = f"""
    # Persona: {state['persona']}
    # Context: {state['context']}
    #
    # Generate aggressive, opinionated post.
    # STRICT JSON:
    # {{"bot_id":"{state['bot_id']}","topic":"{state['topic']}","post_content":"..."}}
    # """
    # return {"output": llm.invoke(prompt).content}

def build_graph():
    g = StateGraph(GraphState)

    g.add_node("decide", decide_node)
    g.add_node("search", search_node)
    g.add_node("generate", generate_node)

    g.set_entry_point("decide")
    g.add_edge("decide", "search")
    g.add_edge("search", "generate")

    # ✅ ADD THIS LINE (VERY IMPORTANT)
    g.set_finish_point("generate")

    return g.compile()

# from langgraph.graph import StateGraph
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
# #OPENAI_API_KEY = os.getenv("CEREBRAS_API_KEY")
#
# llm = ChatOpenAI(
#     api_key=os.getenv("CEREBRAS_API_KEY"),
#     base_url="https://api.cerebras.ai/v1",
#     model="llama3.1-8b",
#     temperature=0.7)
#
#
# def decide_node(state):
#     prompt = f"""
#     Persona: {state['persona']}
#     Decide a trending topic to post about.
#     Return only topic.
#     """
#     topic = llm.invoke(prompt).content
#     return {"topic": topic}
#
#
# def search_node(state):
#     topic = state['topic']
#
#     if "AI" in topic:
#         context = "OpenAI released GPT-5"
#     elif "crypto" in topic:
#         context = "Bitcoin hits ATH"
#     else:
#         context = "Global news"
#
#     return {"context": context}
#
#
# def generate_node(state):
#     prompt = f"""
#     Persona: {state['persona']}
#     Context: {state['context']}
#
#     Generate a strong tweet.
#     Output JSON strictly:
#     {{"bot_id":"{state['bot_id']}","topic":"{state['topic']}","post_content":"..."}}
#     """
#     return {"output": llm.invoke(prompt).content}
#
#
# def build_graph():
#     g = StateGraph(dict)
#
#     g.add_node("decide", decide_node)
#     g.add_node("search", search_node)
#     g.add_node("generate", generate_node)
#
#     g.set_entry_point("decide")
#     g.add_edge("decide", "search")
#     g.add_edge("search", "generate")
#
#     return g.compile()