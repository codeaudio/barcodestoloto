import asyncio

from fastapi import FastAPI, Request, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from services import extract_data_from_barcode

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/barcode/check", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.post("/barcode/check", response_class=HTMLResponse)
async def read_item(request: Request, file: bytes = File(...)):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, extract_data_from_barcode, file)
    return templates.TemplateResponse(
        'index.html', {"request": request} | result
    )
