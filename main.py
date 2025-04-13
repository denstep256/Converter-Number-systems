def convert_to_decimal(number_str: str, base: int) -> int:
    """Переводит число из системы счисления `base` в десятичную систему."""
    return int(number_str, base)

def convert_from_decimal(number: int, base: int) -> str:
    """Переводит десятичное число в систему счисления `base`."""
    if number == 0:
        return "0"
    digits = []
    while number > 0:
        digits.append(str(number % base))
        number //= base
    return ''.join(reversed(digits))

def add_numbers(a: int, b: int) -> int:
    return a + b

def subtract_numbers(a: int, b: int) -> int:
    return a - b

def get_base(prompt: str) -> int:
    while True:
        try:
            base = int(input(prompt))
            if 2 <= base <= 36:
                return base
            else:
                print("Пожалуйста, введите основание системы счисления от 2 до 36.")
        except ValueError:
            print("Неверный ввод. Введите целое число.")

def get_number(prompt: str) -> str:
    return input(prompt).strip().upper()

def main_menu():
    print("=== КОНВЕРТЕР СИСТЕМ СЧИСЛЕНИЯ И КАЛЬКУЛЯТОР ===")
    print("1. Перевести число в другую систему счисления")
    print("2. Сложить или вычесть два числа")
    print("0. Выйти")

def conversion_menu():
    number = get_number("Введите число для перевода: ")
    from_base = get_base("Введите систему счисления этого числа (от 2 до 36): ")
    to_base = get_base("Введите систему счисления, в которую нужно перевести (от 2 до 36): ")

    try:
        decimal_number = convert_to_decimal(number, from_base)
        result = convert_from_decimal(decimal_number, to_base)
        print(f"\nРезультат: {number} (в СС {from_base}) = {result} (в СС {to_base})\n")
    except ValueError:
        print("Ошибка: Неверный формат числа для указанной системы счисления.")

def calculation_menu():
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")

    operation = input("Введите номер операции (1 или 2): ")
    if operation not in {"1", "2"}:
        print("Неверный выбор операции.")
        return

    num1 = get_number("Введите первое число: ")
    base1 = get_base("Введите систему счисления первого числа: ")

    num2 = get_number("Введите второе число: ")
    base2 = get_base("Введите систему счисления второго числа: ")

    try:
        dec1 = convert_to_decimal(num1, base1)
        dec2 = convert_to_decimal(num2, base2)

        if operation == "1":
            result = add_numbers(dec1, dec2)
            op_symbol = "+"
        else:
            result = subtract_numbers(dec1, dec2)
            op_symbol = "-"

        print(f"\nРезультат: {dec1} {op_symbol} {dec2} = {result} (в десятичной системе)\n")
    except ValueError:
        print("Ошибка: Одно из чисел неверно для указанной системы счисления.")

def main():
    while True:
        main_menu()
        choice = input("Выберите действие (0-2): ")

        if choice == "1":
            conversion_menu()
        elif choice == "2":
            calculation_menu()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

        input("Нажмите Enter, чтобы продолжить...\n")

if __name__ == "__main__":
    main()
