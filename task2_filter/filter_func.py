def filter_strings(filter_func, strings):
    # Фильтруем строки с помощью переданной функции
    return [s for s in strings if filter_func(s)]

if __name__ == "__main__":
    data = ["apple", "banana", "a test", "tree", "ant", "no space"]

    no_spaces = filter_strings(lambda x: " " not in x, data)  # Без пробелов
    not_start_with_a = filter_strings(lambda x: not x.lower().startswith("a"), data)  # Не начинаются с "a"
    length_ge_5 = filter_strings(lambda x: len(x) >= 5, data)  # Длина >= 5

    print("No spaces:", no_spaces)
    print("Not start with 'a':", not_start_with_a)
    print("Length >= 5:", length_ge_5)