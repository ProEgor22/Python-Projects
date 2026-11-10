from math import isfinite

def triangle_existence_check(triangle_side_a, triangle_side_b, triangle_side_c):

    if (not all(isfinite(side) and side > 0 
        for side in (triangle_side_a, triangle_side_b, triangle_side_c))
        or (triangle_side_a + triangle_side_b <= triangle_side_c)
        or (triangle_side_a + triangle_side_c <= triangle_side_b)
        or (triangle_side_b + triangle_side_c <= triangle_side_a)
        ):
        return False
    
    else:
        return True