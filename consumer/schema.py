from pydantic import BaseModel
from pydantic import Field


class DefaultRequest(BaseModel):
    ping: str = Field(description="Ping")
