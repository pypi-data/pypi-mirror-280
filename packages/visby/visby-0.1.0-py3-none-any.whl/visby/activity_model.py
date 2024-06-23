from datetime import datetime, timedelta

from sqlmodel import Field, SQLModel


class ActivityBase(SQLModel):
    type: str
    value: float
    duration: timedelta
    user_id: int = Field(default=None, foreign_key="user.user_id")
    created_at: datetime


class Activity(ActivityBase, table=True):  # type: ignore
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    activity_id: int = Field(default=None, primary_key=True)


class ActivityCreate(ActivityBase):
    pass


class ActivityRead(ActivityBase):
    activity_id: int
