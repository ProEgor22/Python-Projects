from height import calculate_height_to_triangle_side_c
from median import calculate_median_to_triangle_side_c

calculations = 0

while True:
    try:
        calculations += 1
        print(f"\n---Розрахунок {calculations}---\n")
        triangle_side_a = float(input("Введіть сторону a: "))
        triangle_side_b = float(input("Введіть сторону b: "))
        triangle_side_c = float(input("Введіть сторону c: "))

        height_to_triangle_side_c = calculate_height_to_triangle_side_c(
                triangle_side_a, triangle_side_b, triangle_side_c
                )
            
        median_to_triangle_side_c = calculate_median_to_triangle_side_c(
                triangle_side_a, triangle_side_b, triangle_side_c
                )

        if (height_to_triangle_side_c == None or median_to_triangle_side_c == None):
            print(f"\nПри a = {triangle_side_a}, b = {triangle_side_b}, "
                  f"c = {triangle_side_c}: Трикутник не існує!")
            
        else:
            print(f"\nПри a = {triangle_side_a}, b = {triangle_side_b}, "
                f"c = {triangle_side_c}: Висота (hc) = {height_to_triangle_side_c:.2f}, "
                f"Медіана (mc) = {median_to_triangle_side_c:.2f}")

    except ValueError:
        print("\nПомилка: Будь ласка, введіть коректне число!")
        calculations -= 1

    user_ans = input("\nБажаєте продовжити? (y/n): ")   
    if user_ans.strip().casefold() != "y":
        break