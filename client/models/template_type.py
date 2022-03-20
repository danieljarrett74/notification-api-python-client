from enum import Enum


class TemplateType(str, Enum):
    COGNITO = "COGNITO"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
