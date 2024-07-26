from fastapi import FastAPI, Request, APIRouter, Form
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from typing import Annotated

from operations.class_selection import router as class_selection_router
from operations.task_selection import router as task_selection_router
from operations.addquestions import router as addquestions_router
from operations.arithmetic import router as arithmetic_router
from operations.equation import router as equation_router
from operations.statistics import router as statistics_router
from operations.task_incresed_complexity import router as task_incresed_complexity_router
from operations.text_task import router as text_task_router
from operations.mixed_tasks import router as mixed_tasks_router
from operations.geometry import router as geometry_router
from operations.count_select import router as count_select_router
from operations.home_teacher import router as home_teacher_router
from operations.home_user import router as home_user_router

app = FastAPI(
    title="Fractions Web API",
)

router = APIRouter()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory='static'), name='static')


@router.get("/")
async def auth(request: Request):
    return templates.TemplateResponse("auth.html", {'request': request})


@router.post("/")
async def auth(request: Request, email_teacher: Annotated[str, Form()] = None,
               password_teacher: Annotated[str, Form()] = None,
               email_user: Annotated[str, Form()] = None,
               password_user: Annotated[str, Form()] = None):
    if email_teacher == 'example@gmail.com' and password_teacher == 'admin':
        redirect_url = request.url_for('home_teacher')
        return RedirectResponse(redirect_url)
    elif email_user == 'example@gmail.com' and password_user == 'admin':
        redirect_url = request.url_for('home_user')
        return RedirectResponse(redirect_url)



app.include_router(router)
app.include_router(class_selection_router)
app.include_router(task_selection_router)
app.include_router(addquestions_router)
app.include_router(arithmetic_router)
app.include_router(equation_router)
app.include_router(statistics_router)
app.include_router(task_incresed_complexity_router)
app.include_router(text_task_router)
app.include_router(mixed_tasks_router)
app.include_router(geometry_router)
app.include_router(count_select_router)
app.include_router(home_teacher_router)
app.include_router(home_user_router)
