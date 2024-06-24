from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str


class User(UserBase, table=True):  # type: ignore
    user_id: int = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    user_id: int
