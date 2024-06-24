from agent.exception.exception_constants import exception_constants


class ParameterMissingException(Exception):
    def __init__(self, code: str = exception_constants.PARAMETER_MISSING_EXCEPTION,
                 message: str = exception_constants.PARAMETER_MISSING_EXCEPTION_MSG):
        self.code = code
        self.message = message


class ParameterVerifyException(Exception):
    def __init__(self, code: str = exception_constants.PARAMETER_VERIFY_EXCEPTION,
                 message: str = exception_constants.PARAMETER_VERIFY_EXCEPTION_MSG):
        self.code = code
        self.message = message


class TextModerationException(Exception):
    def __init__(self, code: str = exception_constants.TEXT_MODERATION_EXCEPTION,
                 message: str = exception_constants.TEXT_MODERATION_VIOLENCE_MSG):
        self.code = code
        self.message = message


class ContainsChineseException(Exception):
    def __init__(self, code: str = exception_constants.CONTAINS_CHINESE_EXCEPTION,
                 message: str = exception_constants.CONTAINS_CHINESE_EXCEPTION_MSG):
        self.code = code
        self.message = message


class CommonException(Exception):
    def __init__(self, code: str = exception_constants.INNER_EXCEPTION,
                 message: str = exception_constants.INNER_EXCEPTION_MSG):
        self.code = code
        self.message = message

