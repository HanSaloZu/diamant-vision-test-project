from pydantic import BaseModel, Field


class NewIssueSchema(BaseModel):
    text: str = Field(min_length=10)


class IssueSchema(BaseModel):
    id: int
    status: str
    sentiment: str
    category: str
    geo: str | None
