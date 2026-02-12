fruits = {"apple": 4, "banana": 5, "citrone": 10}

operand = input("Що робимо зі словником? (del / add / found): ")

if operand == "add":
    newFruit = input("Новий фрукт: ")
    numFruit = int(input("Кількість нового фрукту: "))

    fruits[newFruit] = numFruit
    print(fruits)

elif operand == "found":
    elementSearch = input("Який фрукт шукаємо: ")

    if elementSearch in fruits:
        print("Кількість фруктів:", fruits[elementSearch])
    else:
        print(f"{elementSearch} немає в списку")

    print(fruits)

elif operand == "del":
    elementDelete = input("Що видаляємо: ")

    if elementDelete in fruits:
        fruits.pop(elementDelete)
        print("Видалено.")
    else:
        print("Такого фрукта немає.")

    print(fruits)

else:
    print("Помилка! Спробуйте ще раз.")
