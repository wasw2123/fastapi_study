from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.apis.v1.meeting_router import edgedb_router as meeting_edgedb_router
from app.apis.v1.meeting_router import mysql_router as meeting_mysql_router
from app.apis.v1.participant_router import edgedb_router as participant_edgedb_router
from app.apis.v1.participant_router import mysql_router as participant_mysql_router
from app.configs.tortoise_config import initialize_tortoise

app = FastAPI(
    default_response_class=ORJSONResponse,
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai",  # 에디터 테마 변경 (인식률 향상)
        "persistAuthorization": True,
        "tryItOutEnabled": True,
    },
)

app.include_router(meeting_edgedb_router)
app.include_router(participant_edgedb_router)
app.include_router(meeting_mysql_router)
app.include_router(participant_mysql_router)

initialize_tortoise(app)
