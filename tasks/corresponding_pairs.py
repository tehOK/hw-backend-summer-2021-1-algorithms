from typing import TypeVar

__all__ = ("corresponding_pairs",)


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def corresponding_pairs(arr1: list[T1], arr2: list[T2]) -> list[tuple[T1, T2]]:
    min_len = min(len(arr1), len(arr2))
    return [(arr1[i], arr2[i]) for i in range(min_len)]
