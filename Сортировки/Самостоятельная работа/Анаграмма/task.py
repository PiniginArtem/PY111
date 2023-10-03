def is_anagram(s: str, t: str) -> bool:

    if not s or not t:
        raise ValueError
    if not isinstance(s, str) or not isinstance(s, str):
        raise TypeError

    return sorted(s) == sorted(t)
