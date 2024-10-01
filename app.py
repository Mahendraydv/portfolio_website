from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setting up Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    portfolio_items = [
        {"title": "Project 1", "description": "This is the first project", "url": "#"},
        {"title": "Project 2", "description": "This is the second project", "url": "#"},
        {"title": "Project 3", "description": "This is the third project", "url": "#"},
    ]
    return templates.TemplateResponse("index.html", {"request": request, "portfolio_items": portfolio_items})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})