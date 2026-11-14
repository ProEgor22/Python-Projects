from math import cos, tan, sqrt, acos
import tkinter as tk

def button_func():
    background_colour = "green"
    try:
    
        x = float(entry_x.get())

        if x < -2:
            y = (2**x) * cos(3 * x) - tan(1.5 * x)
            result_interval = "x < -2"
            result_formula = "y = (2**x) * cos(3 * x) - tan(1.5 * x)"
        elif x > 2:
            y = tan(sqrt(x))**2 - 1 / (x + 2.5)
            result_interval = "x > 2"
            result_formula = "y = tan(sqrt(x))**2 - 1 / (x + 2.5)"
        else:
            y = 4.1 * acos(x / 2) + sqrt(x + 2)
            result_interval = "-2 <= x <= 2"
            result_formula = "y = 4.1 * acos(x / 2) + sqrt(x + 2)"

        result_y = f"y = {y:.4f}"

    except ValueError:
        result_y = "Помилка!"
        result_interval = "—"
        result_formula = "Введіть число!"
        background_colour = "red"
    except Exception:
        result_y = "Помилка!"
        result_interval = "—"
        result_formula = "Помилка обчислення!"
        background_colour = "red"      

    entry_y.config(state="normal")
    entry_y.delete(0, tk.END)
    entry_y.insert(0, result_y)
    entry_y.config(disabledforeground=background_colour, state="disabled")

    entry_interval.config(state="normal")
    entry_interval.delete(0, tk.END)
    entry_interval.insert(0, result_interval)
    entry_interval.config(disabledforeground=background_colour, state="disabled")

    entry_formula.config(state="normal")
    entry_formula.delete(0, tk.END)
    entry_formula.insert(0, result_formula)
    entry_formula.config(disabledforeground=background_colour, state="disabled")

root = tk.Tk()

root.title("Lab10 Варіант 16")
root.geometry("480x300")

main_frame = tk.Frame(root)
main_frame.pack(padx=55, pady=35, anchor="nw")

label_x = tk.Label(main_frame, text="Введіть x:", font=("Arial", 12))
label_x.grid(row=0, column=0, padx=5, pady=10, sticky="w")

entry_x = tk.Entry(main_frame, width=30,
                   font=("Arial", 12), justify="center"
                   )
entry_x.grid(row=0, column=1, padx=5, pady=10)

interval = tk.Label(main_frame, text="Проміжок:", font=("Arial", 12))
interval.grid(row=1, column=0, padx=5, pady=10, sticky="w")

entry_interval = tk.Entry(main_frame, width=30,
                          font=("Arial", 12), state="disabled", justify="center"
                          )
entry_interval.grid(row=1, column=1, padx=5, pady=10)

formula = tk.Label(main_frame, text="Формула:", font=("Arial", 12))
formula.grid(row=2, column=0, padx=5, pady=10, sticky="w")

entry_formula = tk.Entry(main_frame, width=30,
                         font=("Arial", 12), state="disabled", justify="center"
                         )
entry_formula.grid(row=2, column=1, padx=5, pady=10)

label_y = tk.Label(main_frame, text="Результат y:", font=("Arial", 12))
label_y.grid(row=3, column=0, padx=5, pady=10, sticky="w")

entry_y = tk.Entry(main_frame, width=30,
                   font=("Arial", 12), state="disabled", justify="center"
                   )
entry_y.grid(row=3, column=1, padx=5, pady=10)

btn = tk.Button(main_frame, text="Обчислити",
                command=button_func, font=("Arial", 12)
                )
btn.grid(row=4, column=0, padx=5, pady=10, columnspan=2)

root.mainloop()