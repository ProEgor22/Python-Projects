from math import sqrt, isfinite

calculations = 0

while True:
    try:
        calculations += 1
        print(f"\n---Розрахунок {calculations}---\n")
        
        triangle_side_a = float(input("Введіть сторону a: "))
        triangle_side_b = float(input("Введіть сторону b: "))
        triangle_side_c = float(input("Введіть сторону c: "))

        if (not all(isfinite(side) and side > 0 
            for side in (triangle_side_a, triangle_side_b, triangle_side_c))
            or (triangle_side_a + triangle_side_b <= triangle_side_c)
            or (triangle_side_a + triangle_side_c <= triangle_side_b)
            or (triangle_side_b + triangle_side_c <= triangle_side_a)
            ):
            print(f"\nПри a = {triangle_side_a}, b = {triangle_side_b}, "
                              f"c = {triangle_side_c}: Трикутник не існує!")

        else:
            triangle_half_perimeter = (triangle_side_a 
                                        + triangle_side_b
                                        + triangle_side_c) / 2
            
            height_to_side_c = (2 / triangle_side_c) * sqrt(max(0.0, triangle_half_perimeter
                                * (triangle_half_perimeter - triangle_side_a) 
                                * (triangle_half_perimeter - triangle_side_b)
                                * (triangle_half_perimeter - triangle_side_c)))
            
            median_to_side_c = 0.5 * sqrt(max(0.0, 2 * triangle_side_a**2
                                              + 2 * triangle_side_b**2 - triangle_side_c**2))
            
            print(f"\nПри a={triangle_side_a}, b={triangle_side_b}, c={triangle_side_c}: "
                  f"Висота (hc)={height_to_side_c:.2f}, Медіана (mc)={median_to_side_c:.2f}")
    except ValueError:
        print("\nПомилка: Будь ласка, введіть коректне число!")
        calculations -= 1

    user_ans = input("\nБажаєте продовжити? (y/n): ")   
    if user_ans.strip().casefold() != "y":
        break