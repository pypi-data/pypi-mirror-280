from pydantic import Field


class Unset:  # noqa: WPS306
    def __bool__(self) -> bool:
        """Make always false.

        Returns:
            bool: _description_
        """
        return False


UnsetField = Field(default_factory=Unset)
