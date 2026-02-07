from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    new_d: dict[KV, KT] = dict()

    for key, value in d.items():
        new_d[value] = key

    return new_d


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    new_d: dict[KV, list[KT]] = dict()

    for key, value in d.items():
        if value in new_d:
            new_d[value].append(key)
        else:
            new_d[value] = [key]

    return new_d
