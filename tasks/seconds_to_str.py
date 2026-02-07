__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    days = seconds // 86400
    remaining = seconds % 86400
    hours = remaining // 3600
    minutes = (remaining % 3600) // 60
    sec = remaining % 60
    to_str = []

    if days:
        to_str.append(f"{days:02d}d")
    if hours or days:
        to_str.append(f"{hours:02d}h")
    if minutes or hours or days:
        to_str.append(f"{minutes:02d}m")
    to_str.append(f"{sec:02d}s")

    return "".join(to_str)
