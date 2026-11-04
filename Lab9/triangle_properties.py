from math import sqrt

def triangle_properties(a, b, c):
    """
    Обчислює висоту трикутника (hc) проведену зi сторони c та
    довжину вiдповiдної медiани (mc).
    Аргумент:
     a (float): сторона 1.
     b (float): сторона 2.
     c (float): сторона 3.
    Повертає:
     tuple: Список, що мiстить (висоту трикутника (hc),
     довжину вiдповiдної медiани (mc)).
    """
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return None, None

    p = (a + b + c) / 2
    hc = (2 / c) * sqrt(p * (p - a) * (p - b) * (p - c))
    mc = 0.5 * sqrt(2 * a**2 + 2 * b**2 - c**2)

    return hc, mc