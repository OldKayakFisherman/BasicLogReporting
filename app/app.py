from fastapi import Depends, FastAPI
from app.models import AnalyzerConfiguration
from app.db import create_db_and_tables
from app.models import UserDB
from app.users import auth_backend, current_active_user, fastapi_users
from services import  ImportValidatorService
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(fastapi_users.get_register_router(), prefix="/auth", tags=["auth"])
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/analyze")
async def analyze(conf: AnalyzerConfiguration):
    validation_response = ImportValidatorService().validateImport(conf)
    if not validation_response.IsValid:
        return JSONResponse(status_code=422, content=",".join(validation_response.Messages))
    else:
        return {"message": "Ok"}


@app.get("/authenticated-route")
async def authenticated_route(user: UserDB = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()

