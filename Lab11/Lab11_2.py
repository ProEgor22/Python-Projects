from math import exp

list_start = 0
list_end = 1
step = 0.1 * (list_end - list_start)
reference_value = 4.1

num_total_value = 0
num_multiplication_value = 1
x = list_start

print("\n--- Табулювання функції y = exp(-2 * x) ---\n"
      "-----------------------------\n"
      "|   x   |          y        |\n"
      "-----------------------------\n")

while x <= list_end + step/2:
    x_rounded = round(x, 3)
    y = exp(-2 * x_rounded)

    print(f"| {x:^5.2f} | {y:^17.4f} |")

    if y > reference_value:
        num_total_value += 1
        num_multiplication_value *= y
    x += step

print("-----------------------------\n"
      "\n--- Результати умовного обчислення ---\n"
       f"Умова: y > {reference_value}\n"
       f"Кількість значень, що відповідають умові: {num_total_value}")

if num_total_value <= 1:
    print(f"Добутку немає!")
else:
    print(f"Добуток цих значень y: {num_multiplication_value:.4f}")

print("--------------------------------------")