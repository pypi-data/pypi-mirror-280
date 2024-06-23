class OmieRequestError(Exception):
    def __init__(self, status_code: int, code: str, message: str) -> None:
        self.status_code = status_code
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return self.message


class OmieBlockedError(Exception):
    pass


class OmieRateLimitError(Exception):
    pass
