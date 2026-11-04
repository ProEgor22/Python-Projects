import triangle_properties

i = 0

while True:
    try:
        i += 1
        print(f"\nРозрахунок {i}\n")
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        c = float(input("Введіть сторону c: "))

        hc, mc = triangle_properties.triangle_properties(a, b, c)

        if hc is None or mc is None:
            print(f"\nПри a={a}, b={b}, c={c}: Трикутник не існує!")
        else:
            print(f"\nПри a={a}, b={b}, c={c}: "
                  f"Висота (hc)={hc:.2f}, Медіана (mc)={mc:.2f}")

    except ValueError:
        print("\nПомилка: Будь ласка, введіть коректне число!")
        i -= 1

    user_ans = input("\nБажаєте продовжити? (y/n): ")   
    if user_ans.casefold() != "y":
        break