from dataclasses import dataclass, field


@dataclass
class ResultDto:
    data: any = None
    errors: list = field(default_factory=list)
    statusmessage: str = None
    entities: list = field(default_factory=list)
    success: bool = False
    rowcount: int = 0
