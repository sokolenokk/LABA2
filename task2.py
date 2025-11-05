def reverse_str(string: str) -> str:
    return string[::-1]

user_string = input("Введите строку: ")
reverse_string = reverse_str(user_string)

print("Перевернутая строка: ", reverse_string)
