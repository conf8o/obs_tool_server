import obsws_python as obs
from obsws_python.error import OBSSDKRequestError
from obs_req_client import obs_req_client, OBSErrorContent
from pydantic import BaseModel
from dataclasses import dataclass


class SceneSectionMutationBoby(BaseModel):
    current_scene: str | None

@dataclass
class SceneSection:
    req_client: obs.ReqClient

    def save(self, body: SceneSectionMutationBoby):
        if body.current_scene:
            try:
                self.req_client.set_current_program_scene(body.current_scene)
            except OBSSDKRequestError as e:
                return ("Error", OBSErrorContent.from_sdk_error(e))

        return ("OK", body)


scene_section = SceneSection(obs_req_client)
