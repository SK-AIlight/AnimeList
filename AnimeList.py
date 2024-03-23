import json
import os

# Получаем абсолютный путь к файлу JSON
file_path = os.path.join(os.path.dirname(__file__), 'animdata.json')

# Загрузка данных из файла (если файл существует)
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, 'r') as file:
        try:
            AnimData = json.load(file)
        except json.JSONDecodeError:
            AnimData = []
else:
    AnimData = []

while True:
    choice = input('Выберите действие, 1 - добавить, 2 - посмотреть, 3 - удалить, 4 - выйти: ')

    if choice == '1':
        name = input("Введите название: ")
        rating = input("Введите рейтинг от 1 до 10: ")
        try:
            rating = float(rating)
            if 1.0 <= rating <= 10.0:
                AnimData.append({"название": name, "рейтинг": rating})
                print("Аниме успешно добавлено!")
            else:
                print("Рейтинг должен быть от 1 до 10!")
        except ValueError:
            print("Рейтинг должен быть числом!")
    elif choice == '2':
        if AnimData:
            sorted_anime = sorted(AnimData, key=lambda x: x["рейтинг"], reverse=True)
            print("Список аниме по рейтингу:")
            for anime in sorted_anime:
                print(f"{anime['название']}: {anime['рейтинг']}")
        else:
            print("Список аниме пуст.")
    elif choice == '3':
        if AnimData:
            print("Список аниме:")
            for index, anime in enumerate(AnimData, start=1):
                print(f"{index}. {anime['название']}: {anime['рейтинг']}")
            to_delete = input("Введите полное название аниме, которое хотите удалить: ")
            deleted = False
            for anime in AnimData:
                if anime["название"] == to_delete:
                    AnimData.remove(anime)
                    print(f"Аниме '{to_delete}' успешно удалено.")
                    deleted = True
                    break
            if not deleted:
                print(f"Аниме '{to_delete}' не найдено в списке.")
        else:
            print("Список аниме пуст.")
    elif choice == '4':
        print("Выход из программы.")
        # Сохранение данных в файл перед выходом
        with open(file_path, 'w') as file:
            json.dump(AnimData, file, ensure_ascii=False)
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите одно из предложенных действий (1, 2, 3 или 4).")
