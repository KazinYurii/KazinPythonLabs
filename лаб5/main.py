def custom_sort_key(word):
    ua_alphabet = " аабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    en_alphabet = " abcdefghijklmnopqrstuvwxyz"

    # Привести слово до нижнього регістру
    lower_word = word.lower()

    # Визначити ключ сортування
    sort_key = []
    for char in lower_word:
        if char in en_alphabet:
            sort_key.append((0, en_alphabet.index(char)))  # Латинські літери мають вищий пріоритет
        elif char in ua_alphabet:
            sort_key.append((1, ua_alphabet.index(char)))  # Українські літери
        else:
            sort_key.append((2, ord(char)))  # Інші символи (якщо є)

    return sort_key


def custom_sort(words):
    return sorted(words, key=custom_sort_key)


def main():
    input_file = "input.txt"

    # Спроба прочитати файл
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            # Зчитуємо список слів із файлу
            my_list = [line.strip() for line in file if line.strip()]
        
        print("Заданий список:")
        print(my_list)

        # Сортування
        sorted_list = custom_sort(my_list)

        print("\nВідсортований список:")
        print(sorted_list)

    except FileNotFoundError:
        print(f"Помилка: файл '{input_file}' не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
