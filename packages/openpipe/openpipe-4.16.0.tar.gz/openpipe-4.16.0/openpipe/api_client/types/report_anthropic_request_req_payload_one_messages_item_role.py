# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ReportAnthropicRequestReqPayloadOneMessagesItemRole(str, enum.Enum):
    USER = "user"
    ASSISTANT = "assistant"

    def visit(self, user: typing.Callable[[], T_Result], assistant: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReportAnthropicRequestReqPayloadOneMessagesItemRole.USER:
            return user()
        if self is ReportAnthropicRequestReqPayloadOneMessagesItemRole.ASSISTANT:
            return assistant()
