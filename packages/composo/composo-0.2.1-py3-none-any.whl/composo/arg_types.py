
@dataclass
class StrParam(ParameterBase):
    param_type: Literal[ParameterType.STRING] = ParameterType.STRING

    def __init__(self, description=None):
        self.description = description

    def cast(self, value):
        return str(value)


@dataclass
class IntParam(ParameterBase):
    param_type: Literal[ParameterType.INTEGER] = ParameterType.INTEGER

    allowableMin: Optional[int] = None
    allowableMax: Optional[int] = None

    def __init__(self, description=None, min=None, max=None):
        # Create an instance of the IntParam class
        self.description = description

        self.allowableMin: int = min
        self.allowableMax: int = max

    def validate(self, value):
        if self.allowableMin and not value >= self.allowableMin:
            raise ComposoUserException(
                f"Parameter is invalid. Value {value} does not exceed minimum value: {self.allowableMin}"
            )

        if self.allowableMax and not value <= self.allowableMax:
            raise ComposoUserException(
                f"Parameter is invalid. Value {value} exceeds maximum value: {self.allowableMax}"
            )

        return value

    def cast(self, item):
        return int(item)


@dataclass
class FloatParam(ParameterBase):
    param_type: Literal[ParameterType.FLOAT] = ParameterType.FLOAT

    allowableMin: Optional[float] = None
    allowableMax: Optional[float] = None

    def __init__(self, description=None, min=None, max=None):
        self.description = description

        self.allowableMin: float = min
        self.allowableMax: float = max

    def validate(self, value):
        if self.allowableMin and not value >= self.allowableMin:
            raise ComposoUserException(
                f"Parameter is invalid. Value {value} does not exceed minimum value: {self.allowableMin}"
            )

        if self.allowableMax and not value <= self.allowableMax:
            raise ComposoUserException(
                f"Parameter is invalid. Value {value} exceeds maximum value: {self.allowableMax}"
            )

        return value

    def cast(self, item):
        return float(item)


@dataclass
class MultiChoiceStrParam(ParameterBase):
    param_type: Literal[ParameterType.MULTICHOICESTRING] = ParameterType.MULTICHOICESTRING
    choices: List[str] = None

    def __init__(self, choices: List[str] = None, description=None):
        self.description = description
        self.choices = choices

    def validate(self, value):
        if self.choices is not None:
            if value not in self.choices:
                raise ComposoUserException(
                    f"Parameter is invalid. Value {value} is not in the list of allowable values: {self.choices}"
                )

        return value

    def cast(self, item):
        return str(item)


@dataclass
class ConversationHistoryParam(ParameterBase):
    param_type: Literal[ParameterType.CONVERSATIONHISTORY] = ParameterType.CONVERSATIONHISTORY

    def __init__(self, description=None):
        self.description = description

    def validate(self, value):
        if not isinstance(value, list):
            raise ComposoUserException(f"ConversationHistoryParam is invalid. Must be a list")
        if not all(isinstance(item, dict) for item in value):
            raise ComposoUserException(f"ConversationHistoryParam is invalid. Must be a list of dicts")
        return value

    def cast(self, item):
        return item


WORKABLE_TYPES = Union[StrParam, IntParam, FloatParam, MultiChoiceStrParam, ConversationHistoryParam]

