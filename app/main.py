from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uuid

app = FastAPI()

# Serve static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Use Jinja2 for HTML templates
templates = Jinja2Templates(directory="templates")

orders = {}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/place-order")
async def place_order(order: dict):
    order_id = str(uuid.uuid4())[:8] 
    orders[order_id] = order
    return {"order_id": order_id, **order}
