from pydantic import BaseModel

from pyfunvice.common_func import get_uuid


class RequestModel(BaseModel):
    requestId: str


class ResponseModel:
    def __init__(
        self, requestId: str, code: str, message: str, data: dict = None
    ) -> None:
        if requestId is None or len(requestId) == 0:
            requestId = get_uuid()
        self.requestId: str = requestId
        self.code: str = code
        self.message: str = message
        self.data: dict = data

    def to_dict(self) -> dict:
        obj_dict = {
            "requestId": self.requestId,
            "code": self.code,
            "message": self.message,
            "data": self.data,
        }

        return obj_dict
