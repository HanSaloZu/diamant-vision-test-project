from .Base import Base
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum
from sqlalchemy import Integer, DateTime, Text
import datetime


class StatusEnum(str, Enum):
    open = "open"
    closed = "closed"


class SentimentEnum(str, Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"
    unknown = "unknown"


class CategoryEnum(str, Enum):
    technical = "техническая"
    payment = "оплата"
    other = "другое"


class IssueModel(Base):
    __tablename__ = "issues"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[StatusEnum] = mapped_column(default=StatusEnum.open, nullable=False)
    timestamp: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
    )
    sentiment: Mapped[SentimentEnum] = mapped_column(nullable=False)
    category: Mapped[CategoryEnum] = mapped_column(
        default=CategoryEnum.other, nullable=False
    )
    geo: Mapped[str] = mapped_column(nullable=True)
