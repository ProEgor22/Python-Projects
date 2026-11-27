from math import isfinite

def determine_if_num_is_even(number):
    return number % 2 == 0

def calculate_rectangle_area(width, height):
    return width * height

def calculate_num_to_the_power(base, exponent):
    return base ** exponent

def count_words(sentence):
    return len(sentence.split())

def define_wind_properties(velocity):
    speed = abs(velocity)
    if speed < 1:
        return "Штиль"
    elif speed < 5:
        return "Слабкий"
    elif speed < 9:
        return "Помірний"
    elif speed < 19:
        return "Сильний"
    return "Ураган"

while True:
    try:
        usr_startup_ans = int(input(
            "\nВведіть номер завдання або 0 для завершення програми (2, 3, 4, 5, 6): "
            ))

        match usr_startup_ans:
            case 0:
                print("\nПрограма завершена.")
                break

            case 2:
                while True:
                    print("\n----Завдання №2: Перевірка на парність----")
                    try:
                        number = int(input("\nВведіть бажане число: "))
                        is_even_result = determine_if_num_is_even(number)

                        if is_even_result:
                            print("\nЧисло парне!")
                        else:
                            print("\nЧисло непарне!")

                    except ValueError:
                        print("\nВведіть ціле число!!!")
                        continue

                    break

            case 3:
                while True:
                    print("\n----Завдання №3: Площа прямокутника----")
                    try:
                        rect_width = float(input("\nВведіть ширину прямокутника: "))
                        rect_height = float(input("Введіть висоту прямокутника: "))

                        if not all((
                            isfinite(rect_width), isfinite(rect_height),
                            rect_width > 0, rect_height > 0
                            )):
                            raise ValueError

                        rect_surface_area = calculate_rectangle_area(rect_width, rect_height)
                        print(f"\nПлоща прямокутника: {rect_surface_area:.2f}")

                    except ValueError:
                        print("\nВведіть число > 0!")
                        continue

                    break

            case 4:
                while True:
                    print("\n----Завдання №4: Піднесення до степеня----")
                    # УВАГА: float зберігає лише ~15-17 значущих цифр, тому для результатів,
                    # більших за ~10^16, цифри після цього порогу будуть неточними.
                    try:
                        base = float(input("\nВведіть число, що підноситься до степеня: "))
                        exponent = float(input("Введіть степінь: "))

                        if not all((isfinite(base), isfinite(exponent))):
                            raise ValueError

                        result_num = calculate_num_to_the_power(base, exponent)
                        print(f"\nРезультат: {result_num:.2f}")
                        
                    except ValueError:
                        print("\nВведіть число!")
                        continue
                    except OverflowError:
                        print("\nРезультат виходить за допустимі межі!")
                        continue
                    except ZeroDivisionError:
                        print("\nПомилка! Ділення на 0!")
                        continue

                    break

            case 5:
                while True:
                    print("\n----Завдання №5: Кількість слів----")
                    sentence = input("\nВведіть слова через пробіл: ")

                    if not sentence.strip():
                        print("\nРечення порожнє!")
                        continue

                    words_value = count_words(sentence)
                    print(f"\nВведено слів: {words_value}")

                    break

            case 6:
                while True:
                    print("\n----Завдання №6: Параметри вітру----")
                    try:
                        wind_velocity = float(input("\nВведіть швидкість вітру: "))

                        if not isfinite(wind_velocity):
                            raise ValueError

                        wind_status = define_wind_properties(wind_velocity)
                        print(f"\nВітер: {wind_status}")

                    except ValueError:
                        print("\nВведіть число!")
                        continue

                    break

            case _:
                print("\nВведено неіснуючий варіант!")

    except ValueError:
        print("Введіть ціле число!")