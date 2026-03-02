from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.dtos.get_meeting_response import GetMeetingResponse
from app.services.meeting_service_edgedb import service_create_meeting_edgedb
from app.services.meeting_service_mysql import service_create_meeting_mysql

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["meeting"])
# 이부분
# 실전에서는 어떤 db를 사용하는지 url에 적을 필요가 없음
# 강의에서만 사용 이유는 데이터를 한 디비에서만 사용하기 위함


@edgedb_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_edgedb()).url_code)


@mysql_router.post("", description="meeting을 생성하비다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_mysql()).url_code)


@edgedb_router.get("/{meeting_url_code}", description="meeting을 조회합니다.")
async def api_get_meeting_edgedb(meeting_url_code: str) -> GetMeetingResponse:
    return GetMeetingResponse(url_code="abc")


@mysql_router.get("/{meeting_url_code}", description="meeting을 조회합니다.")
async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:
    return GetMeetingResponse(url_code="abc")
