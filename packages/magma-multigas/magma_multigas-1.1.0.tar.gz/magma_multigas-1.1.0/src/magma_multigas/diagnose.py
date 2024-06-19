from typing import List
from .multigas_data import MultiGasData
from .validator import validate_mutligas_data_type

COLUMNS: List[str] = [
    'Licor_volts',
    'Licor_bench_temp',
    'Licor_pressure',
]

class Diagnose:
    def __init__(self, two_seconds: MultiGasData):
        validate_mutligas_data_type(two_seconds.type_of_data)

        self.df = two_seconds.df_original
        self.licor_volts = two_seconds.df_original['licor_volts']
        self.licor_bench_temp = two_seconds.df_original['licor_bench_temp']
        self.licor_pressure = two_seconds.df_original['licor_pressure']