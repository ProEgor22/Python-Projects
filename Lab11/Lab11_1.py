from math import isfinite
from time import sleep

while True:
    try:
        match_code = int(input("Введіть бажане завдання (0 - завершення програми, 2, 3, 4, 5, 6): "))
        
        match match_code:
            case 0:
                print("\nПрограма завершена.\n")
                break
            case 2:
                #----Zavdanya 2----
                num_list = []
                i = 0

                while i <= 10:
                    if i % 2 != 0:
                        num_list.append(i)
                    i += 1

                print(f"\nЕлементи: {num_list}\n")

            case 3:
                #----Zavdanya 3----
                num_list = []
                i = 0

                while i <= 20:
                    if i % 2 == 0:
                        num_list.append(i)
                    i += 1

                print(f"\nЕлементи: {num_list}\n")
            
            case 4:
                #----Zavdanya 4----
                num_list = []
                num_sum = 0

                while True:
                    try:
                        number = float(input("\nВведіть число: "))

                        if not isfinite(number):
                            raise ValueError
                        elif number == 0:
                            print("\nВведення завершено.\n")
                            break

                        num_list.append(number)
                        num_sum += number
                        print(f"Масив: {num_list}\n"
                            f"Сума елементів: {round(num_sum, 5)}\n")

                    except ValueError:
                        print("Помилка. Введіть число!!!\n")

            case 5:
                #----Zavdanya 5----
                try:
                    seconds_value = int(input("\nВведіть кількість секунд: "))
                
                    if seconds_value <= 0:
                        print("\nВведіть ціле число > 0!!!\n")
                        continue

                    while seconds_value > 0:
                        print(f"Залишилось {seconds_value} сек.")
                        sleep(1)
                        seconds_value -= 1

                    print("Час вийшов!!!\n")

                except ValueError:
                    print("\nВведіть число!!!\n")
                    continue

            case 6:
                #----Zavdanya 6----
                list_start = -2.25          # Початок
                list_end = -2               # Кінець
                step = 0.05                 # Крок
                constant_term = 74.2        # Вільний член

                number = list_start
                while number <= list_end + step / 2:
                    x_rounded = round(number, 2)
                    y = 0.0084 * (x_rounded**(5/4) + constant_term) / (x_rounded**2 + 3.62)
                    print(f"\nЗначення: x = {x_rounded}, y = {y:.4f}\n")
                    number += step

            case _:
                print("Обраний варіант не існує!!!")
    except ValueError:
        print("Введіть ціле число!!!")
        continue