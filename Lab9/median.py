from math import sqrt
from triangle_check import triangle_existence_check

def calculate_median_to_triangle_side_c(
    triangle_side_a, triangle_side_b, triangle_side_c
    ):

    triangle_existence = triangle_existence_check(
        triangle_side_a, triangle_side_b, triangle_side_c
        )

    if not triangle_existence:
        return None

    median_to_side_c = 0.5 * sqrt(max(0.0, 2 * triangle_side_a**2
                                  + 2 * triangle_side_b**2 - triangle_side_c**2))
    
    return median_to_side_c