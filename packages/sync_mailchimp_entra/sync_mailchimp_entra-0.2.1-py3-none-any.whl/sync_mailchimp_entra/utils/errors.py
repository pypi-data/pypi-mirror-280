import json

class Error:
    title: str
    status: int
    detail: str
    instance: str

    def __init__(self, title: str, status: int, detail: str, instance: str):
        self.title = title
        self.status = status
        self.detail = detail
        self.instance = instance

def deserial_error(error_json):
    return Error(**json.loads(error_json))