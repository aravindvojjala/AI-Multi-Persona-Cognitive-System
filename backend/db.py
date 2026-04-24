import chromadb

client = chromadb.Client(
    settings=chromadb.Settings(persist_directory="./chroma_db")
)

collection = client.get_or_create_collection("bots")