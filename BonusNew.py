import random


# Класс, объект которого является рулеткой.
class Position:
    # Во время создания объекта передаем ему словарь, в котором ключи - строки с названием позиции и ее ценой,
    # а значения - вероятность выпадения.
    def __init__(self, position_dict):
        self.position = position_dict

    # Запуская функцию мы получаем случайный ключ(строку с позицией), в соответствии с вероятностью его выпадения.
    def get_random_name(self):
        position = random.choices(list(self.position.keys()), weights=list(self.position.values()))
        return f"{position[0]}"


if __name__ == '__main__':
    names_dict = {"2 zoom консультации: 5800": 60,
                  "5 zoom консультаций: 9500": 40,
                  "10 zoom консультаций: 14900": 20,
                  "20 zoom консультаций	: 24900": 10}
    positionTest = Position(names_dict)
    print(positionTest.get_random_name())


