from typing import TypeAlias

JSONType: TypeAlias = int | float | str | bool | None | list['JSONType'] | dict[str, 'JSONType']