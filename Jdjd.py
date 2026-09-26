while True:
    try:
        a, op, b = input("> ").split()
        a, b = float(a), float(b)
        print(a + b if op == "+" else a - b if op == "-" else a * b if op == "*" else a / b)
    except:
        print("Ошибка")