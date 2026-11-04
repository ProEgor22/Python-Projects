from math import sqrt

i = 0

while True:
    try:
        i += 1
        print(f"\n---Розрахунок {i}---\n")
        
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        c = float(input("Введіть сторону c: "))

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            print(f"\nПри a={a}, b={b}, c={c}: Трикутник не існує!")
        else:
            p = (a + b + c) / 2
            hc = (2 / c) * sqrt(p * (p - a) * (p - b) * (p - c))
            mc = 0.5 * sqrt(2 * a**2 + 2 * b**2 - c**2)

            print(f"\nПри a={a}, b={b}, c={c}: "
                  f"Висота (hc)={hc:.2f}, Медіана (mc)={mc:.2f}")
    except ValueError:
        print("\nПомилка: Будь ласка, введіть коректне число!")
        i -= 1

    user_ans = input("\nБажаєте продовжити? (y/n): ")   
    if user_ans.casefold() != "y":
        break