def deep_compare(a, b):
    if type(a) != type(b):
        return False

    if isinstance(a, (int, float, str)):
        if a != b:
            return False

    if isinstance(a, list):
        if len(a) != len(b):
            return False
        for element_a, element_b in zip(a, b):
            if not deep_compare(element_a, element_b):
                return False

    if isinstance(a, dict):
        if len(a) != len(b):
            return False
        for key_a, value_a in a.items():
            if key_a not in b.keys():
                return False
            if not deep_compare(a[key_a], b[key_a]):
                return False
    return True

