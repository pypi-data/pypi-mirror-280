# This file was auto-generated by Fern from our API Definition.

import typing

from .report_anthropic_request_req_payload_one import ReportAnthropicRequestReqPayloadOne
from .report_anthropic_request_req_payload_zero import ReportAnthropicRequestReqPayloadZero

ReportAnthropicRequestReqPayload = typing.Union[
    ReportAnthropicRequestReqPayloadZero, ReportAnthropicRequestReqPayloadOne
]
