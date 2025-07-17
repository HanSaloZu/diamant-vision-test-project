from fastapi import APIRouter, Depends, Request, BackgroundTasks
from schemas.Issue import NewIssueSchema, IssueSchema
from models.Issue import IssueModel, CategoryEnum
from database import SessionDep, create_new_session
import aiohttp
from sqlalchemy import select
from http_client import http_client
from config import sentiment_analysis_api_config, ip_api_config, chat_gpt_config

router = APIRouter()


async def update_issue_category(issue_id: int):
    async with create_new_session() as session:
        query = await session.execute(
            select(IssueModel).where(IssueModel.id == issue_id)
        )
        issue = query.scalar_one_or_none()

        httpc = http_client()
        chat_gpt_response = await httpc.post(
            chat_gpt_config.URL,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {chat_gpt_config.API_KEY}",
            },
            json={
                "model": "gpt-4.1-mini",
                "store": False,
                "messages": [
                    {
                        "role": "user",
                        "content": f"Определи категорию жалобы: {issue.text}. Варианты: техническая, оплата, другое. Ответ только одним словом.",
                    }
                ],
            },
        )

        if chat_gpt_response.status == 200:
            json_response = await chat_gpt_response.json()
            try:
                category = json_response["choices"][0]["message"]["content"]
            except (KeyError, IndexError):
                category = "другое"

            if category in [c.value for c in CategoryEnum]:
                issue.category = category
            else:
                issue.category = CategoryEnum.other

        await session.commit()


@router.post("/issues")
async def create_issue(
    new_issue_data: NewIssueSchema,
    session: SessionDep,
    request: Request,
    background_tasks: BackgroundTasks,
    http_client: aiohttp.ClientSession = Depends(http_client),
) -> IssueSchema:
    new_issue = IssueModel(text=new_issue_data.text)

    sentiment_analysis_api_response = await http_client.post(
        sentiment_analysis_api_config.URL,
        headers={"apikey": sentiment_analysis_api_config.API_KEY},
        data=new_issue.text,
    )
    sentiment = "unknown"
    if sentiment_analysis_api_response.status == 200:
        json_response = await sentiment_analysis_api_response.json()
        sentiment = json_response.get("sentiment", "unknown")
    new_issue.sentiment = sentiment

    client_ip = request.client.host
    ip_api_response = await http_client.get(
        f"{ip_api_config.URL}/{client_ip}?fields={ip_api_config.FIELDS}"
    )
    if ip_api_response.status == 200:
        geo_response = await ip_api_response.json()
        if geo_response["status"] == "success":
            geo = f"{geo_response['continent']}, {geo_response['country']}, "
            geo += geo_response["city"]
            new_issue.geo = geo

    session.add(new_issue)
    await session.commit()

    background_tasks.add_task(update_issue_category, new_issue.id)

    return new_issue
