import obsws_python as obs
from obsws_python.error import OBSSDKRequestError
from obs_req_client import obs_req_client, ErrorContent
from pydantic import BaseModel
from dataclasses import dataclass


class MutationBoby(BaseModel):
    current_scene: str | None

@dataclass
class SceneSection:

    req_client: obs.ReqClient
    current_scene: str | None

    def save(self, body: MutationBoby):
        if body.current_scene:
            self.current_scene = body.current_scene
            try:
                self.req_client.set_current_program_scene(self.current_scene)
            except OBSSDKRequestError as e:
                return ("Error", ErrorContent(message=str(e), reason=self.error_code_to_reason(e.code)))

        return ("OK", body)
    
    def error_code_to_reason(self, code) -> str:
        if code == 600:
            return "ResourceNotFound"

scene_section = SceneSection(obs_req_client, obs_req_client.get_current_program_scene().scene_name)
