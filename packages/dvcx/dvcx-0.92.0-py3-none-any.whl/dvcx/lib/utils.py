class DvcxError(Exception):
    def __init__(self, message):
        super().__init__(message)


class DvcxParamsError(DvcxError):
    def __init__(self, message):
        super().__init__(message)
