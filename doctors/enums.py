"""Contains optional choices for
    certain model field."""
from enum import Enum


class SpecialityEnum(Enum):
    """Inherit from generic Enum."""
    
    Urologist = 'Urologist'
    Gynecologist = 'Gynecologist'
    Dermatologist = 'Dermatologist'
    Nephrologist = 'Nephrologist'
    Endocrinologist = 'Endocrinologist'
