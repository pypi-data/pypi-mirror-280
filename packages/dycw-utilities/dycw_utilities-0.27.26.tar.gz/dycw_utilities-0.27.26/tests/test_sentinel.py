from collections.abc import Callable

from pytest import mark, param

from utilities.sentinel import _REPR, Sentinel, sentinel


class TestSentinel:
    def test_isinstance(self) -> None:
        assert isinstance(sentinel, Sentinel)

    @mark.parametrize("method", [param(repr), param(str)])
    def test_repr_and_str(self, method: Callable[..., str]) -> None:
        assert method(sentinel) == _REPR

    def test_singletone(self) -> None:
        assert Sentinel() is sentinel
