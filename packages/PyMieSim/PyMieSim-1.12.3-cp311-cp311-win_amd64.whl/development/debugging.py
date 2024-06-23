import numpy
from typing import List, Union
from pydantic.dataclasses import dataclass

scatterer_set = Sphere(
    diameter=800e-9,
    index=1.44,
    medium_index=1,
    source=source
)

@dataclass
class TestClass:
    string_list: Union[List[str], str]


string_list = ['LP01']
string_list = numpy.asarray(string_list).astype(str)
print(string_list.dtype)
string_list = "LP01"

test_instance = TestClass(string_list=string_list)

print('finished')

# -
