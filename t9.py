def fibonacci(n):
    if n < 0:
        return None 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Яке по порядку число Фібоначчі шукатимемо? "))

result = fibonacci(n)
if result is not None:
    print(f"Число Фібоначчі під номером {n} = {result}")
else:
    print("Некоректне число. Введіть n >= 0")
