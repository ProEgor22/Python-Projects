from math import isfinite, prod
reference_value = 1.7

while True:
    usr_input = input(
        "Введіть масив через кому (дробова частина через крапку, напр.: 1, 2.5, 3):  "
        )

    try:
        num_list_input = [float(x) for x in usr_input.split(",") if x.strip()]
    except ValueError:
        print("\nПомилка! Переконайтеся, що ви ввели лише числа, розділені комами.\n")
        continue

    if not num_list_input:
        print("\nПомилка! Масив порожній.\n")
        continue

    if not all(isfinite(x) for x in num_list_input):
        print("\nПомилка! Значення nan та inf не допускаються.\n")
        continue

    break

num_list_output = [round(x, 4) for x in num_list_input if x >= reference_value]

print("\n---РЕЗУЛЬТАТИ ОБЧИСЛЕННЯ---\n"
      f"Порівняльна константа c = {reference_value}\n"
      f"\nВведено масив: {num_list_input}\n"
      f"\nКількість елементів у вхідному масиві: {len(num_list_input)}\n"
      "---------------------------\n"
      f"Кількість елементів >= c становить: {len(num_list_output)}\n"
      f"\nМасив що обчислюється: {num_list_output}\n"
      )

if len(num_list_output) <= 1:
    print("Добутку немає.\n")
else:
    print(f"Добуток елементів масиву: {prod(num_list_output):.4f}")
print("---------------------------")