class AppException(Exception):
    def __init__(self, data='不合法请求', code=422):
        self.code = code
        self.data = data
