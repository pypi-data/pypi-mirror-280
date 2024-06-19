# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class LocalTestingOnlyGetLatestLoggedCallResponse(pydantic.BaseModel):
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    cache_hit: bool = pydantic.Field(alias="cacheHit")
    status_code: typing.Optional[float] = pydantic.Field(alias="statusCode")
    error_message: typing.Optional[str] = pydantic.Field(alias="errorMessage")
    req_payload: typing.Optional[typing.Any] = pydantic.Field(alias="reqPayload")
    resp_payload: typing.Optional[typing.Any] = pydantic.Field(alias="respPayload")
    tags: typing.Dict[str, typing.Optional[str]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
