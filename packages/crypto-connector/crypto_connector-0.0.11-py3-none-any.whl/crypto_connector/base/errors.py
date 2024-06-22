class BaseError(Exception):
    pass


class ExchangeError(BaseError):
    pass


class NotSupported(ExchangeError):
    pass


class BadResponse(ExchangeError):
    pass


class InvalidOrder(ExchangeError):
    pass


class AuthenticationError(ExchangeError):
    pass


class OrderNotFound(InvalidOrder):
    pass


class ServerError(BaseError):
    pass
