import os
from decorator_fun import time_logger

# Получаем путь к текущей папке скрипта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Полные пути к файлам
INPUT_FILE = os.path.join(BASE_DIR, "input.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "output.txt")

@time_logger
def sum_numbers(a, b):
    result = a + b
    print(f"Sum: {result}")
    return result

@time_logger
def sum_from_file():
    with open(INPUT_FILE, "r") as f:
        a, b = map(int, f.read().split())
    result = a + b
    with open(OUTPUT_FILE, "w") as f:
        f.write(str(result))
    print(f"Sum from file: {result}")
    return result

if __name__ == "__main__":
    sum_numbers(5, 7)
    sum_from_file()
