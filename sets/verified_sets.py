from numbers import Integral


class UniquenessError(KeyError):
    pass


class VerifiedSet:
    def __init__(self, set):
        VerifiedSet._verify(set)
        self.set = set

    def _verify(self):
        raise NotImplementedError

    def __str__(self):
        if self.set:
            return f"{type(self).__name__}({self.set})"
        else:
            return f"{type(self).__name__}()"

    def add(self, par):
        addval = self._verify(par)
        self.set.add(addval)

    def update(self, par):
        updateval = self._verify(par)
        self.set.update(updateval.set)

    def symmetric_difference_update(self, par):
        sym_dif_updval = self._verify(par)
        self.set.symmetric_difference_update(sym_dif_updval.set)

    def union(self, other):
        other = self._verify(other)
        return self.__class__(tuple(self.set.union(other.set)))

    def intersection(self, other):
        other = self._verify(other)
        return self.__class__(tuple(self.set.intersection(other.set)))

    def difference(self, other):
        other = self._verify(other)
        return self.__class__(tuple(self.set.difference(other.set)))

    def symmetric_difference(self, other):
        other = self._verify(other)
        return self.__class__(tuple(self.set.symmetric_difference(other.set)))

    def copy(self):
        return self.__class__(tuple(self.set))


class IntSet(VerifiedSet):
    def __init__(self, tup):
        self.set = set(tup)

    def _verify(self, par):
        if not (isinstance(par, Integral) or isinstance(par, IntSet)):
            raise TypeError(f"IntSet expected an integer or IntSet, got a {type(par).__name__}.")
        else:
            return par


class UniqueSet(VerifiedSet):
    def __init__(self, par):
        self.set = set(par)

    def _verify(self, par):
        if isinstance(par, Integral):
            if par in self.set:
                raise UniquenessError
        elif isinstance(par, set):
            if par.issubset(self.set):
                raise UniquenessError
        else:
            return par
