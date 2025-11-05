while True:
    print("Калькулятор")
    print("Введите выражение в соответствующее поле в формате '5 + 7 - 3', "
          "либо 'Выход' для выхода\n")

    expression = input("Введите выражение: ")

    if expression == "Выход":
        print("Выход")
        break

    try:
        answer = eval(expression)
        print("Ответ: ", answer)
    except(SyntaxError, NameError, ZeroDivisionError):
        print("Ошибка ввода, повторите попытку")

    print()
    print("--------------------------------------")
