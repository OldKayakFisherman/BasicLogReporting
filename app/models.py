from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from fastapi_users import models


class ConfigurationValidationResponse(models.BaseModel):
    IsValid: bool
    Messages: list[str]

    def __init__(self):
        Messages = list[str]()

class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


class CheckAttribute(BaseModel):
    Run: bool
    Threshold: Optional[int] = None
    TimeStart: Optional[str] = None
    TimeEnd: Optional[str] = None
    EventTypeValue: Optional[str] = None


class AnalyzerConfiguration(BaseModel):
    RequestHeaderLogField: str
    UserIdLogField: str
    EventTypeLogField: str
    EventDateLogField: str
    RemoteAddressLogField: str
    SqlInjectionCheck: CheckAttribute
    ExcessiveEventCheck: CheckAttribute
    CrossFrameScriptingCheck: CheckAttribute
    LDAPInjectionCheck: CheckAttribute
    ExcessiveLoginCheck: CheckAttribute
    ExcessivePasswordChangeCheck: CheckAttribute
    LoginAfterHoursCheck: CheckAttribute
    ReportWebInspect: bool
    ReportNessus: bool
    ReportCrossFeed: bool
    Logs: List[Dict[Any, Any]]
