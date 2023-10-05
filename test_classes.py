from BonusNew import Position


def test_probability():
    # Создаем словарь с нужными значениями
    names_dict = {"2 zoom консультации: 5800": 60,
                  "5 zoom консультаций: 9500": 40,
                  "10 zoom консультаций: 14900": 20,
                  "20 zoom консультаций	: 24900": 10}
    # Создаем объект рулетки
    position = Position(names_dict)
    # Создаем счетчик, который будет записывать, сколько раз выпало каждое значение
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(1000):
        names = position.get_random_name()
        if names == '2 zoom консультации: 5800':
            a += 1
        if names == '5 zoom консультаций: 9500':
            b += 1
        if names == '10 zoom консультаций: 14900':
            c += 1
        if names == '20 zoom консультаций	: 24900':
            d += 1
    # Проверяем, соответствует ли количество выпадений нашим требованиям
    assert a > b > c > d
