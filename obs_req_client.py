import obsws_python as obs
from obsws_python.error import OBSSDKRequestError
from pydantic import BaseModel

obs_req_client = obs.ReqClient()

class OBSErrorContent(BaseModel):
    message: str
    reason: str
    
    @staticmethod
    def from_sdk_error(error: OBSSDKRequestError) -> 'OBSErrorContent':
        return OBSErrorContent(message=str(error), reason=error_code_to_reason(error.code))

def error_code_to_reason(code) -> str:
    if code == 600:
        return "ResourceNotFound"
