'''
Two old ladies meet each other with constant speeds V1 and V2 km/h.
Determine the time (in hours) before the old woman meets if the distance between them is equal S Km.
'''

def two_old_ladies(s: float, v1: float, v2: float) -> float:
    formula = s / (v1 + v2)
    return formula

print(two_old_ladies(float(input()), float(input()), float(input())))
