from pydantic import Field

class Unset:
    def __bool__(self) -> bool:
        """Make always false.

        Returns:
            bool: _description_
        """
        return False


UnsetField = Field(default_factory=Unset)