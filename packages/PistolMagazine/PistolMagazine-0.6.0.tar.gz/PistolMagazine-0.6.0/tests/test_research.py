from pprint import pprint

from pistol_magazine import DataMocker, Str, ProviderField
from pistol_magazine.built_in_provider import *


class Param(DataMocker):
    risk_param_type: ProviderField = ProviderField(
        CyclicParameterProvider(parameter_list=[1000, 1031, 1001, 1002, 1009]).get_next_param
    )
    param_value: Str = Str()
    static_param: ProviderField = ProviderField(
        FixedValueProvider(fixed_value="STATIC").get_fixed_value
    )
    f: ProviderField = ProviderField(
        RandomFloatInRangeProvider(start=0.00, end=4.00, precision=4).get_random_float
    )
    i: ProviderField = ProviderField(
        IncrementalValueProvider(start=0, step=2).get_next_value
    )

    def param_info(self):
        return self.mock(num_entries=10, as_list=True)


def test_gen_data():
    data = Param().param_info()
    pprint(data)
