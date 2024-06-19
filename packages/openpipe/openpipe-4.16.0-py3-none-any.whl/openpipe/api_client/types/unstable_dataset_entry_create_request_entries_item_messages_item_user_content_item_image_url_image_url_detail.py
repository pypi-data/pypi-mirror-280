# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UnstableDatasetEntryCreateRequestEntriesItemMessagesItemUserContentItemImageUrlImageUrlDetail(str, enum.Enum):
    AUTO = "auto"
    LOW = "low"
    HIGH = "high"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UnstableDatasetEntryCreateRequestEntriesItemMessagesItemUserContentItemImageUrlImageUrlDetail.AUTO:
            return auto()
        if self is UnstableDatasetEntryCreateRequestEntriesItemMessagesItemUserContentItemImageUrlImageUrlDetail.LOW:
            return low()
        if self is UnstableDatasetEntryCreateRequestEntriesItemMessagesItemUserContentItemImageUrlImageUrlDetail.HIGH:
            return high()
