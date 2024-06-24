class MyError(Exception):
    def __init__(self, err_msg="", status_code=400):
        self.err_msg = err_msg
        self.status_code = status_code
        super().__init__(self.err_msg)


class NotFoundError(MyError):
    def __init__(self, err_msg="", status_code=404):
        super().__init__(err_msg, status_code)


class ParamEmptyError(MyError):
    def __init__(self, err_msg, status_code=400):
        super().__init__(f"{err_msg}不能为空", status_code)


class ParamTypeError(MyError):
    def __init__(self, err_msg, status_code=400):
        super().__init__(f"{err_msg}类型错误", status_code)


class ParamRangeError(MyError):
    def __init__(self, err_msg, status_code=400):
        super().__init__(f"{err_msg}超出允许的范围", status_code)


class ParamFormatError(MyError):
    def __init__(self, err_msg, status_code=400):
        super().__init__(f"{err_msg}格式错误", status_code)


class RequestMethodNotAllowError(MyError):
    def __init__(self, status_code=405):
        super().__init__("不允许的请求方式", status_code)


class RequestActNotAllowError(MyError):
    def __init__(self, status_code=405):
        super().__init__("不允许的请求动作", status_code)


class MethodNeedRedefinedError(MyError):
    def __init__(self, status_code=500):
        super().__init__("使用此方法需要先自定义", status_code)


class PermissionCheckFailedError(MyError):
    def __init__(self, status_code=403):  # HTTP 403 Forbidden
        super().__init__("权限校验失败", status_code)
