from fastapi import FastAPI
from app.agent import graph

app = FastAPI()

@app.get("/")
def agent():
    return graph.invoke({"customer_name": "Cris", "my_var": "Ciao"})