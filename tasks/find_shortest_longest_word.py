import re

__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    words = re.findall(r'[\S]+', text)
    if not words:
        return None, None
    
    short = min(words, key=len)
    long = max(words, key=len)

    return (short, long)