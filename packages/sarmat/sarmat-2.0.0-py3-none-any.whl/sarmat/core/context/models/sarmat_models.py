"""
Sarmat.
Описание сущностей.
Базовый класс для описания моделей.
"""
from dataclasses import asdict, dataclass, fields
from typing import Any, Dict, List, Optional

from sarmat.core.constants import DurationType, IntervalType


@dataclass
class BaseModel:

    @property
    def sarmat_fields(self):
        return [fld.name for fld in fields(self)]

    @property
    def as_dict(self):
        return asdict(self)


@dataclass
class BaseIdModel:

    id: Optional[int] = 0


@dataclass
class BaseUidModel:

    uid: Optional[str] = ""


@dataclass
class BaseCatalogModel:
    """Базовая модель для описания справочников"""

    cypher: str     # шифр (константа)
    name: str       # название


@dataclass
class CustomAttributesModel:

    custom_attributes: Optional[Dict[str, Any]] = None

    @property
    def custom_fields(self) -> List[str]:
        return list(self.custom_attributes.keys()) if self.custom_attributes else []


@dataclass
class PersonModel(BaseModel):
    """Данные человека"""

    last_name: str      # фамилия
    first_name: str     # имя
    middle_name: str    # отчество
    male: bool          # пол: М


@dataclass
class BaseDurationModel(BaseModel):
    """Базовый элемент для описания продолжительности"""

    duration_type: DurationType     # тип продолжительности
    value: int                      # значение
    in_activity: bool               # признак активной фазы


@dataclass
class DurationModel(BaseIdModel, CustomAttributesModel, BaseDurationModel, BaseCatalogModel):
    """Простая модель с описанием продолжительности"""


@dataclass
class DurationItemModel(BaseIdModel, BaseDurationModel):
    """Элемент сложной продолжительности"""

    position: int = 0


@dataclass
class ComplexDurationModel(BaseIdModel, CustomAttributesModel, BaseCatalogModel):
    """Составная модель с описанием продолжительности"""

    values: Optional[list[DurationItemModel]] = None    # последовательность из отрезков времени


@dataclass
class BaseIntervalModel(BaseModel):
    """Базовая модель для описания интервала"""

    interval_type: IntervalType     # тип интервала
    values: List[int]               # список значений
    in_activity: bool               # признак активной фазы


@dataclass
class IntervalModel(BaseIdModel, CustomAttributesModel, BaseIntervalModel, BaseCatalogModel):
    """Простая модель с описанием интервала"""


@dataclass
class IntervalItemModel(BaseIdModel, BaseIntervalModel):
    """Элемент сложного интервала"""

    position: int = 0


@dataclass
class ComplexIntervalModel(BaseIdModel, CustomAttributesModel, BaseCatalogModel):
    """Составная модель с описанием интервала"""

    intervals: Optional[list[IntervalItemModel]] = None     # описание сложного периода
