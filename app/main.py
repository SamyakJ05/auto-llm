from fastapi import FastAPI, Response
import os
from .openai_client import OpenAI

app = FastAPI()
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/run")
async def run(response: Response, task: str = None):
    client = OpenAI(AIPROXY_TOKEN)
    tool_to_use = client.get_tool_to_use(task)
    return tool_to_use


@app.get("/read")
async def read(response: Response, path: str = None):
    if(path is None):
        response.status_code = 404
        return {"message": "Path not found"}
    return {"path": path}