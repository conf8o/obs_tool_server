import obsws_python as obs
from typing import TypedDict


class ErrorContent(TypedDict):
    message: str
    reason: str

obs_req_client = obs.ReqClient()
