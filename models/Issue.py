from .Base import Base
from sqlalchemy.orm import Mapped, mapped_column
import enum
from sqlalchemy import Integer, DateTime, Text, Enum
import datetime


class StatusEnum(str, enum.Enum):
    open = "open"
    closed = "closed"


class SentimentEnum(str, enum.Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"
    unknown = "unknown"


class CategoryEnum(str, enum.Enum):
    technical = "техническая"
    payment = "оплата"
    other = "другое"


class IssueModel(Base):
    __tablename__ = "issues"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[StatusEnum] = mapped_column(
        Enum(StatusEnum), default=StatusEnum.open, nullable=False
    )
    timestamp: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
    )
    sentiment: Mapped[SentimentEnum] = mapped_column(
        Enum(SentimentEnum), nullable=False
    )
    category: Mapped[CategoryEnum] = mapped_column(
        Enum(
            CategoryEnum,
            native_enum=False,
            values_callable=lambda e: [x.value for x in e],
        ),
        default=CategoryEnum.other,
        nullable=False,
    )
    geo: Mapped[str] = mapped_column(nullable=True)
