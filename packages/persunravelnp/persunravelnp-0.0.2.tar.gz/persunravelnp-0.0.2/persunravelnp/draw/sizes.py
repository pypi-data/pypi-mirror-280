from enum import StrEnum
from dataclasses import dataclass
from typing import Optional

class Unit(StrEnum):
    EM = 'em'
    EX = 'ex'
    PX = 'px'
    IN = 'in'
    CM = 'cm'
    MM = 'mm'
    PT = 'pt'
    PC = 'pc'
    PERCENT = '%'

@dataclass(frozen=True, slots=True)
class Length:
    value: float
    unit: Unit

    def __str__(self):
        return '{:.5f}'.format(self.value) + self.unit

@dataclass(frozen=True, slots=True)
class Sizes:
    width:  Optional[Length] = None
    height: Optional[Length] = None

    
