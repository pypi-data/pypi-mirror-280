from sqlmodel import Field, SQLModel, create_engine
from typing import Optional, Dict
from sqlalchemy import JSON, Column
from uuid import UUID
from datetime import datetime


class APIKey(SQLModel, table=True):
    __tablename__ = "api_keys"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: UUID = Field()
    api_key: str = Field()
    salt: str = Field()
    create_time: datetime = Field(default_factory=lambda: datetime.utcnow())
    label: str = Field()


class QueryLog(SQLModel, table=True):
    __tablename__ = "query_logs"
    id: Optional[int] = Field(default=None, primary_key=True)
    query_name: str = Field()
    cost: int = Field()
    timestamp: datetime = Field(default_factory=lambda: datetime.utcnow())
    details: dict = Field(sa_column=Column(JSON), default={})
    user_id: UUID = Field()


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    customer: Optional[str] = Field(default=None)
    user_id: UUID = Field()
    active: bool = Field(default=False)
    state: Optional[str] = Field(default=None)
