from math import sqrt
from triangle_check import triangle_existence_check

def calculate_height_to_triangle_side_c(
    triangle_side_a, triangle_side_b, triangle_side_c
    ):

    triangle_existence = triangle_existence_check(
        triangle_side_a, triangle_side_b, triangle_side_c
        )

    if not triangle_existence:
        return None
    
    triangle_half_perimeter = (triangle_side_a 
                               + triangle_side_b
                               + triangle_side_c) / 2

    height_to_side_c = (2 / triangle_side_c) * sqrt(max(0.0, triangle_half_perimeter
                        * (triangle_half_perimeter - triangle_side_a) 
                        * (triangle_half_perimeter - triangle_side_b)
                        * (triangle_half_perimeter - triangle_side_c)))
    
    return height_to_side_c