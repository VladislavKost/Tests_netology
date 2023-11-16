mentors = [
    [
        "Евгений Шмаргунов",
        "Олег Булыгин",
        "Дмитрий Демидов",
        "Кирилл Табельский",
        "Александр Ульянцев",
        "Александр Бардин",
        "Александр Иванов",
        "Антон Солонилин",
        "Максим Филипенко",
        "Елена Никитина",
        "Азамат Искаков",
        "Роман Гордиенко",
    ],
    [
        "Филипп Воронов",
        "Анна Юшина",
        "Иван Бочаров",
        "Анатолий Корсаков",
        "Юрий Пеньков",
        "Илья Сухачев",
        "Иван Маркитан",
        "Ринат Бибиков",
        "Вадим Ерошевичев",
        "Тимур Сейсембаев",
        "Максим Батырев",
        "Никита Шумский",
        "Алексей Степанов",
        "Денис Коротков",
        "Антон Глушков",
        "Сергей Индюков",
        "Максим Воронцов",
        "Евгений Грязнов",
        "Константин Виролайнен",
        "Сергей Сердюк",
        "Павел Дерендяев",
    ],
    [
        "Евгений Шмаргунов",
        "Олег Булыгин",
        "Александр Бардин",
        "Александр Иванов",
        "Кирилл Табельский",
        "Александр Ульянцев",
        "Роман Гордиенко",
        "Адилет Асканжоев",
        "Александр Шлейко",
        "Алена Батицкая",
        "Денис Ежков",
        "Владимир Чебукин",
        "Эдгар Нуруллин",
        "Евгений Шек",
        "Максим Филипенко",
        "Елена Никитина",
    ],
    [
        "Владимир Чебукин",
        "Эдгар Нуруллин",
        "Евгений Шек",
        "Валерий Хаслер",
        "Татьяна Тен",
        "Александр Фитискин",
        "Александр Шлейко",
        "Алена Батицкая",
        "Александр Беспоясов",
        "Денис Ежков",
        "Николай Лопин",
        "Михаил Ларченко",
    ],
]


def get_unique_names(mentors):
    all_list = []

    for i in mentors:
        all_list += i

    all_names_list = []
    for mentor in all_list:
        name = mentor[: (mentor.find(" "))]
        all_names_list.append(name)
    unique_names = set(all_names_list)
    all_names_sorted = sorted(unique_names)
    return f"Уникальные имена преподавателей: {', '.join(all_names_sorted)}."
