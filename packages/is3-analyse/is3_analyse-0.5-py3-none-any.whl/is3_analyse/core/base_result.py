from .util import to_json_serializable


def success(message: str | None = None, data=None):
    if message is not None:
        return BaseResult(BaseResult.SUCCESS[0], message, data)
    return BaseResult(*BaseResult.SUCCESS, data)


def failed(code: int | None = None, message: str | None = None):
    if code is not None and message is not None:
        return BaseResult(code, message)
    if message is not None:
        return BaseResult(BaseResult.FAILED[0], message)
    return BaseResult(*BaseResult.FAILED)


class BaseResult:
    SUCCESS = (200, "操作成功")
    FAILED = (500, "操作失败")

    def __init__(self, code: int, message: str, data=None):
        self.code = code
        self.message = message
        self.data = data

    def __dict__(self):
        self.data = to_json_serializable(self.data)
        return {
            'code': self.code,
            'msg': self.message,
            'data': self.data
        }
