from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["meeting"])
# 이부분
# 실전에서는 어떤 db를 사용하는지 url에 적을 필요가 없음
# 강의에서만 사용 이유는 데이터를 한 디비에서만 사용하기 위함


@edgedb_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.post("", description="meeting을 생성하비다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")
