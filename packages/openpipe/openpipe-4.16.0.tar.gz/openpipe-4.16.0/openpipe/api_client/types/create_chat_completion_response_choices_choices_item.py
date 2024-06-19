# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .create_chat_completion_response_choices_choices_item_finish_reason import (
    CreateChatCompletionResponseChoicesChoicesItemFinishReason,
)
from .create_chat_completion_response_choices_choices_item_logprobs import (
    CreateChatCompletionResponseChoicesChoicesItemLogprobs,
)
from .create_chat_completion_response_choices_choices_item_message import (
    CreateChatCompletionResponseChoicesChoicesItemMessage,
)

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateChatCompletionResponseChoicesChoicesItem(pydantic.BaseModel):
    finish_reason: CreateChatCompletionResponseChoicesChoicesItemFinishReason
    index: float
    message: CreateChatCompletionResponseChoicesChoicesItemMessage
    logprobs: typing.Optional[CreateChatCompletionResponseChoicesChoicesItemLogprobs]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
