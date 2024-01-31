from pydantic import BaseModel, field_validator, field_serializer
from datetime import datetime


class Log(BaseModel):
    timestamp: datetime | str
    name: str
    client_ip: str
    client_name: None | str
    type: None | str

    @field_validator("timestamp")
    @classmethod
    def ensure_timestamp(cls, v: str):
        parsed_date = datetime.strptime(v, "%d-%b-%Y %H:%M:%S.%f")
        return parsed_date

    @field_serializer("timestamp")
    def serialize_timestamp(timestamp: datetime) -> str:
        return timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
