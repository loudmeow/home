
def read_last(lines, file):
    if not isinstance(lines, int) or lines < 1:
        print("Введено неправльное значение.")
        return
    try:
        with open(file, 'r', encoding='utf-8') as f:
            file_lines = f.readlines()
            start_index = max(0, len(file_lines) - lines)
            for line in file_lines[start_index:]:
                print(line.strip())
    except FileNotFoundError:
        print("Такого файла нет.")
read_last(2, 'text1')\
lines = input()





filename = input("Введите имя файла: ")
if not filename.endswith(".txt"):
    filename = filename + ".txt"
with open(filename, "w") as f:
    while True:
        line = input("Введите строку для записи в файл:n")
        if line == "":
            print("Файл сохранен успешно.")
            break
        f.write(line + "n")