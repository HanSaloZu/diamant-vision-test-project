from fastapi import APIRouter, Depends, Request
from schemas.Issue import NewIssueSchema, IssueSchema
from models.Issue import IssueModel
from database import SessionDep
import aiohttp
from http_client import http_client
from config import sentiment_analysis_api_config, ip_api_config

router = APIRouter()


@router.post("/issues")
async def create_issue(
    new_issue_data: NewIssueSchema,
    session: SessionDep,
    request: Request,
    http_client: aiohttp.ClientSession = Depends(http_client),
) -> IssueSchema:
    new_issue = IssueModel(text=new_issue_data.text)
    sentiment_analysis_api_response = await http_client.post(
        sentiment_analysis_api_config.URL,
        headers={"apikey": sentiment_analysis_api_config.API_KEY},
        data=new_issue.text,
    )

    sentiment = "unknown"
    if (
        sentiment_analysis_api_response.status >= 200
        and sentiment_analysis_api_response.status < 400
    ):
        json_response = await sentiment_analysis_api_response.json()
        sentiment = json_response.get("sentiment", "unknown")
    new_issue.sentiment = sentiment

    client_ip = request.client.host
    ip_api_response = await http_client.get(
        f"{ip_api_config.URL}/{client_ip}?fields={ip_api_config.FIELDS}"
    )
    if ip_api_response.status >= 200 and ip_api_response.status < 400:
        geo_response = await ip_api_response.json()
        if geo_response["status"] == "success":
            geo = f"{geo_response['continent']}, {geo_response['country']}, "
            geo += geo_response["city"]
            new_issue.geo = geo

    session.add(new_issue)
    await session.commit()

    return new_issue
