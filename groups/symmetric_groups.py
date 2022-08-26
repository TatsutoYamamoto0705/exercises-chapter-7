from example_code.groups import Group
import numpy as np


class SymmetricGroup(Group):
    symbol = "S"

    def _validate(self, value):
        if not (isinstance(value, np.ndarray) and sorted(value) == list(range(self.n))):
            raise ValueError("Element value must be a sequence containing "
                             "0 to order-1.")

    def operation(self, a, b):
        final_list = np.array([a[b] for b in b])
        return final_list
