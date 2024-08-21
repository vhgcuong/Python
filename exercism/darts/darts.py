from math import sqrt


def score(x, y):
    radius = sqrt((x)**2 + (y)**2)
    if radius <= 1.0: return 10
    if 1.0 < radius <= 5.0: return 5
    if 5.0 < radius <= 10.0: return 1
    return 0
