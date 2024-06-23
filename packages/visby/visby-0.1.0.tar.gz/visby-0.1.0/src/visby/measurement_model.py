from datetime import datetime

from sqlmodel import Field, SQLModel


class MeasurementBase(SQLModel):
    type: str
    value: float
    user_id: int = Field(default=None, foreign_key="user.user_id")
    created_at: datetime


class Measurement(MeasurementBase, table=True):  # type: ignore
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    measurement_id: int = Field(default=None, primary_key=True)


class MeasurementCreate(MeasurementBase):
    pass


class MeasurementRead(MeasurementBase):
    measurement_id: int
