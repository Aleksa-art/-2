# data_processing.py
fruits = {"apple": 4, "banana": 5, "citrone": 10}

def add_fruit(name, quantity):
    fruits[name] = quantity
    return fruits

def find_fruit(name):
    return fruits.get(name, None)

def delete_fruit(name):
    if name in fruits:
        fruits.pop(name)
        return True
    return False
  
# io_operations.py
def get_input(prompt):
    return input(prompt)

def print_dict(d):
    print(d)

def print_message(msg):
    print(msg)

# checks.py
def check_even(num):
    return num % 2 == 0

def check_div3(num):
    return num % 3 == 0
  
# main.py
import data_processing as dp
import io_operations as io

operand = io.get_input("Що робимо зі словником? (del / add / found): ")

if operand == "add":
    name = io.get_input("Новий фрукт: ")
    quantity = int(io.get_input("Кількість нового фрукту: "))
    dp.add_fruit(name, quantity)
    io.print_dict(dp.fruits)

elif operand == "found":
    name = io.get_input("Який фрукт шукаємо: ")
    result = dp.find_fruit(name)
    if result is not None:
        io.print_message(f"Кількість фруктів: {result}")
    else:
        io.print_message(f"{name} немає в списку")

elif operand == "del":
    name = io.get_input("Що видаляємо: ")
    if dp.delete_fruit(name):
        io.print_message("Видалено.")
    else:
        io.print_message("Такого фрукта немає.")
    io.print_dict(dp.fruits)

else:
    io.print_message("Помилка! Спробуйте ще раз.")
