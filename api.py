from fastapi import FastAPI
from Topic import bert_topic

app = FastAPI()

@app.post("/analyze")
def analyze(url: str):
    result = bert_topic(url)
    return {"results": result}
