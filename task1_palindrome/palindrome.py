def is_palindrome(s: str) -> bool:
    # Убираем пробелы и регистр, оставляем только буквы и цифры
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Сравниваем строку с её обратной версией
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_strings = ["level", "Anna", "A man a plan a canal Panama", "hello"]
    for string in test_strings:
        print(f"{string}: {is_palindrome(string)}")
