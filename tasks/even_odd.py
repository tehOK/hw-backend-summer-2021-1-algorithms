__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    even = 0
    odd = 0
    for number in numbers:
        if (number % 2) > 0:
            odd += number
        else:
            even += number
    if odd == 0 or even == 0:
        return 0
    return even / odd