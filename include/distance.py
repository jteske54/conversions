#  Made by Jacob Teske June 2016
from enum import Enum

class Distance(Enum):
    METER = 1.0
    KILOMETER = 1e3
    MEGAMETER = 1e6
    CENTIMETER = 1e-2
    MILLIMETER = 1e-3
    MICROMETER = 1e-6
    NANOMETER = 1e-9
    PICOMETER = 1e-12
    INCH = 0.0254
    FOOT = 0.3048
    YARD = 0.9144

def convert(value: float, unit: Distance, to_unit: Distance, precision: int = 4) -> float:
    return round(value * unit.value / to_unit.value, precision)

if __name__ == '__main__':
    number = 5900
    units = Distance.YARD
    to_units = Distance.KILOMETER
    answer = convert(number, units, to_units)
    print(answer)