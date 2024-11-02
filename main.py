from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/send")
def send(rusuk: int, jenis: str):
    r = requests.post(f'http://54.175.220.82:8080/function/lab-{jenis}', json={"rusuk": rusuk})
    result = int(r.json()["luas"])
    return {
        "result": result,
    }