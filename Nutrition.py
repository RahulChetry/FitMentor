import tkinter as tk
from tkinter import messagebox, ttk

NUTRITION_DB = {
    "Vegetarian": {
        "Rice": {"Calories": 130, "Protein": 2.7, "Carbs": 28, "Fat": 0.3},
        "Broccoli": {"Calories": 55, "Protein": 3.7, "Carbs": 11, "Fat": 0.6},
        "Wheat": {"Calories": 340, "Protein": 13, "Carbs": 72, "Fat": 2.5},
        "Daal": {"Calories": 116, "Protein": 9, "Carbs": 20, "Fat": 0.4},
        "Paneer": {"Calories": 265, "Protein": 18, "Carbs": 6, "Fat": 20},
        "Potato": {"Calories": 77, "Protein": 2, "Carbs": 17, "Fat": 0.1},
        "Spinach": {"Calories": 23, "Protein": 2.9, "Carbs": 3.6, "Fat": 0.4},
        "Carrot": {"Calories": 41, "Protein": 0.9, "Carbs": 10, "Fat": 0.2},
    },
    "Non-Vegetarian": {
        "Chicken": {"Calories": 239, "Protein": 27, "Carbs": 0, "Fat": 14},
        "Mutton": {"Calories": 294, "Protein": 25, "Carbs": 0, "Fat": 21},
        "Fish": {"Calories": 206, "Protein": 22, "Carbs": 0, "Fat": 12},
        "Prawn": {"Calories": 99, "Protein": 24, "Carbs": 0.2, "Fat": 0.3},
        "Egg": {"Calories": 155, "Protein": 13, "Carbs": 1.1, "Fat": 11},
    },
    "Drinks": {
        "Juice": {"Calories": 45, "Protein": 0.7, "Carbs": 10, "Fat": 0.2},
        "Cold Drink": {"Calories": 40, "Protein": 0, "Carbs": 10, "Fat": 0},
        "Alcohol": {"Calories": 70, "Protein": 0, "Carbs": 0, "Fat": 0},
        "Beer": {"Calories": 43, "Protein": 0.5, "Carbs": 3.6, "Fat": 0},
        "Milk": {"Calories": 42, "Protein": 3.4, "Carbs": 5, "Fat": 1},
    },
}

def open_category(category):
    global current_category
    current_category = category
    meal_var.set("")
    update_meal_menu(category)
    entry_quantity.delete(0, tk.END)
    result_text.set("")
    result_frame.pack_forget()
    frame_home.pack_forget()
    frame_meal.pack(fill="both", expand=True)

def update_meal_menu(category):
    menu = meal_menu["menu"]
    menu.delete(0, "end")
    for meal in NUTRITION_DB[category]:
        menu.add_command(label=meal, command=lambda m=meal: meal_var.set(m))

def calculate_nutrition():
    meal = meal_var.get()
    quantity = entry_quantity.get()

    if not meal or not quantity:
        messagebox.showerror("Error", "Please select a meal and enter a quantity.")
        return

    try:
        quantity = float(quantity)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be a number.")
        return

    if meal not in NUTRITION_DB[current_category]:
        messagebox.showerror("Error", f"Meal '{meal}' not found in the database.")
        return

    nutrition = NUTRITION_DB[current_category][meal]
    calories = nutrition["Calories"] * (quantity / 100)
    protein = nutrition["Protein"] * (quantity / 100)
    carbs = nutrition["Carbs"] * (quantity / 100)
    fat = nutrition["Fat"] * (quantity / 100)

    result_text.set(
        f"🌱 Category: {current_category}\n🥗 Meal: {meal}\n💧 Quantity: {quantity}g/ml\n\n"
        f"🔥 Calories: {calories:.2f} kcal\n💪 Protein: {protein:.2f} g\n"
        f"🍞 Carbs: {carbs:.2f} g\n🥑 Fat: {fat:.2f} g"
    )

    result_frame.pack(pady=10, padx=20)

def clear_inputs():
    meal_var.set("")
    entry_quantity.delete(0, tk.END)
    result_text.set("")
    result_frame.pack_forget()

def go_back():
    frame_meal.pack_forget()
    frame_home.pack(fill="both", expand=True)

def start_app():
    frame_welcome.pack_forget()
    frame_home.pack(fill="both", expand=True)

root = tk.Tk()
root.title("FitMentor - Nutritional Calculator")
root.geometry("900x700")
root.resizable(True, True)

frame_welcome = tk.Frame(root, bg="#ffcc80")
frame_welcome.pack(fill="both", expand=True)

tk.Label(
    frame_welcome,
    text="🎉Welcome to FitMentor 🎉",
    font=("Comic Sans MS", 36, "bold"),
    bg="#ffcc80",
    fg="#d84315",
    pady=100,
).pack()

tk.Label(
    frame_welcome,
    text="Track your meals and nutrition easily",
    font=("Comic Sans MS", 24),
    bg="#ffcc80",
    fg="#3e2723",
    pady=20,
).pack()

btn_start = tk.Button(
    frame_welcome,
    text="Start Planning",
    command=start_app,
    bg="#7e57c2",
    fg="white",
    font=("Comic Sans MS", 24, "bold"),
    width=20,
    height=2,
)
btn_start.pack(pady=50)

frame_home = tk.Frame(root, bg="#ffcc80")

tk.Label(
    frame_home,
    text="🧑‍🍳 Select a Category 🍽",
    font=("Comic Sans MS", 36, "bold"),
    bg="#ffcc80",
    fg="#d84315",
    pady=20,
).pack()

btn_veg = tk.Button(
    frame_home,
    text="🌿 Vegetarian",
    command=lambda: open_category("Vegetarian"),
    bg="#81c784",
    fg="white",
    font=("Comic Sans MS", 24, "bold"),
    width=20,
    height=2,
)
btn_veg.pack(pady=15)

btn_nonveg = tk.Button(
    frame_home,
    text="🍗 Non-Vegetarian",
    command=lambda: open_category("Non-Vegetarian"),
    bg="#f06292",
    fg="white",
    font=("Comic Sans MS", 24, "bold"),
    width=20,
    height=2,
)
btn_nonveg.pack(pady=15)

btn_drinks = tk.Button(
    frame_home,
    text="🥤 Drinks",
    command=lambda: open_category("Drinks"),
    bg="#4fc3f7",
    fg="white",
    font=("Comic Sans MS", 24, "bold"),
    width=20,
    height=2,
)
btn_drinks.pack(pady=15)

frame_meal = tk.Frame(root, bg="#ffe082")

tk.Label(
    frame_meal,
    text="🤔 Select Meal and Quantity 📏",
    font=("Comic Sans MS", 28, "bold"),
    bg="#ffe082",
    fg="#f57f17",
    pady=20,
).pack()

meal_var = tk.StringVar(frame_meal)
meal_menu = tk.OptionMenu(frame_meal, meal_var, "")
meal_menu.config(width=25, font=("Comic Sans MS", 14), bg="#ffeb3b", fg="#3e2723")
meal_menu.pack(pady=10)

tk.Label(frame_meal, text="Enter Quantity (grams/mL):", bg="#ffe082", font=("Arial", 16)).pack(pady=5)
entry_quantity = tk.Entry(frame_meal, width=30, font=("Arial", 14))
entry_quantity.pack(pady=5)

btn_calculate = tk.Button(
    frame_meal,
    text="📊 Calculate",
    command=calculate_nutrition,
    bg="#7e57c2",
    fg="white",
    font=("Comic Sans MS", 18, "bold"),
    width=15,
)
btn_calculate.pack(pady=15)

result_frame = tk.Frame(frame_meal, bg="white", bd=2, relief="solid")
result_frame.pack_forget()
result_text = tk.StringVar()
tk.Label(result_frame, textvariable=result_text, justify="left", font=("Arial", 14), bg="white", wraplength=600).pack(pady=10)

btn_clear = tk.Button(
    frame_meal,
    text="🗑 Clear",
    command=clear_inputs,
    bg="#c62828",
    fg="white",
    font=("Comic Sans MS", 18, "bold"),
    width=10,
)
btn_clear.pack(side="left", padx=10, pady=20)

btn_back = tk.Button(
    frame_meal,
    text="🔙 Back",
    command=go_back,
    bg="#d84315",
    fg="white",
    font=("Comic Sans MS", 18, "bold"),
    width=10,
)
btn_back.pack(side="right", padx=10, pady=20)

current_category = "Vegetarian"
update_meal_menu(current_category)
root.mainloop()