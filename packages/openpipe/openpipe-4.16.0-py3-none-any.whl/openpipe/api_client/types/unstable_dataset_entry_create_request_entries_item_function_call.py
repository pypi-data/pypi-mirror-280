# This file was auto-generated by Fern from our API Definition.

import typing

import typing_extensions

from .unstable_dataset_entry_create_request_entries_item_function_call_name import (
    UnstableDatasetEntryCreateRequestEntriesItemFunctionCallName,
)

UnstableDatasetEntryCreateRequestEntriesItemFunctionCall = typing.Union[
    typing_extensions.Literal["none"],
    typing_extensions.Literal["auto"],
    UnstableDatasetEntryCreateRequestEntriesItemFunctionCallName,
]
