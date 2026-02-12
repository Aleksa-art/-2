calc = lambda a, b, op: a + b if op == "sum" else a * b if op == "mul" else a - b if op == "sub" else None

print(calc(5, 3, "sum"))  # 8
print(calc(5, 3, "mul"))  # 15
print(calc(5, 3, "sub"))  # 2
