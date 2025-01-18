from math import ceil, floor

def half_max(x: float) -> float:
    return ceil(x) + floor(x)

print(half_max(float(input())))
