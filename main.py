from obs_req_client import OBSErrorContent
import obs_scene
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()

class SceneSectionError(Exception):
    def __init__(self, request=BaseModel, error: OBSErrorContent={}):
        self.request = request
        self.error = error

@app.exception_handler(SceneSectionError)
def handle_scene_section_error(_, exc: SceneSectionError):
    error = exc.error
    if error.reason == "ResourceNotFound":
        return JSONResponse(status_code=400, content={"request_body": exc.request.model_dump(), "error_content": error.model_dump()})

class PutSceneSectionRequest(BaseModel):
    current_scene: str

    def to_domain(self) -> obs_scene.SceneSectionMutationBoby:
        return obs_scene.SceneSectionMutationBoby(current_scene=self.current_scene)

@app.put("/scene_section")
def put_scene_section(put_scene_section_request: PutSceneSectionRequest):
    match obs_scene.scene_section.save(put_scene_section_request.to_domain()):
        case ("OK", result):
            return result
        case ("Error", error):
            raise SceneSectionError(put_scene_section_request, error)
