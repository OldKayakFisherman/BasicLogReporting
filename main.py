from fastapi import FastAPI
from datetime import time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel

app = FastAPI()


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


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/analyze")
async def analyze(conf: AnalyzerConfiguration):
    return  {"message": "Ok"}
