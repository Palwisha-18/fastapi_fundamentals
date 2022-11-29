from typing import Optional

from fastapi import APIRouter, Request, Form, Depends, Cookie
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from starlette.responses import HTMLResponse

from db import get_session
from routers.cars import get_cars

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request, cars_cookie: Optional[str] = Cookie(None)):
    print(cars_cookie)
    return templates.TemplateResponse("home.html",
                                      {"request": request})


@router.post("/search", response_class=HTMLResponse)
def search(*, size: str = Form(...), doors: int = Form(...),
           request: Request,
           session: Session = Depends(get_session)):
    cars = get_cars(size=size, doors=doors, session=session)
    return templates.TemplateResponse("search_results.html",
                                      {"request": request, "cars": cars})