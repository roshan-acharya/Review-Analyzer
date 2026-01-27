from fastapi import FastAPI
from Pipeline import get_result

app = FastAPI()

@app.post("/analyze")
def analyze(url: str):
    result = get_result(url)
    return {"results": result}
