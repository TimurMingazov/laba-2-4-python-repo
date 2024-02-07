class Animal:
    def __init__(self, name: str, age: int, weight: float):
        """
        Конструктор базового класса "Животное".

        :param name: Кличка животного.
        :param age: Возраст живтного.
        :param weight: Вес животного.
        """
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self) -> str:
        """
        метод, возвращающий строковое представление объекта.

        :return: Строковое представление объекта.
        """
        return f"{self.name} {self.age} ({self.weight})"

    def __repr__(self) -> str:
        """
        метод, возвращающий строковое представление объекта для отладки.

        :return: Строковое представление объекта для отладки.
        """
        return f"Animal(name={self.name}, age={self.age}, weight={self.weight})"

    def sound(self):
        """
        метод для вывода звука, издающих животными

        :return: Строковое представление объекта.
        """
        print("I make a sound")

    def movement(self):
        """
        метод для вывода движений, которые могут выполнять жвиотные

        :return: Строковое представление объекта.
        """
        print("I can move")


class Cat(Animal):
    def __init__(self, name: str, age: int, weight: float, breed: str):
        """
        Конструктор дочернего класса "Кот".

        :param name: Кличка животного.
        :param age: Возраст живтного.
        :param weight: Вес животного.
        :param breed: Порода.
        """
        super().__init__(name, age, weight)
        self.breed = breed

    def __str__(self) -> str:
        """
        метод, возвращающий строковое представление объекта.

        :return: Строковое представление объекта.
        """
        return f"I am {self.name} of {self.age} years. I am {self.weight} kg. My breed is {self.breed}"

    def sound(self):
        """
        метод для вывода звука, издающих животными

        :return: Строковое представление объекта.
        """
        print("Meow")

    def movement(self):
        """
        метод для вывода движений, которые могут выполнять жвиотные

        :return: Строковое представление объекта.
        """
        print("I can run, jump and climb trees")


class Dog(Animal):
    def __init__(self, name: str, age: int, weight: float, breed: str, occupation: str):
        """
        Конструктор дочернего класса "Собака".

        :param name: Кличка животного.
        :param age: Возраст живтного.
        :param weight: Вес животного.
        :param breed: Порода.
        :param occupation: Деятельность собаки (поводырь, охотничья, пастух и т.д.).
        """
        super().__init__(name, age, weight)
        self.occupation = occupation
        self.breed = breed

    def __str__(self) -> str:
        """
        метод, возвращающий строковое представление объекта.

        :return: Строковое представление объекта.
        """
        return f"I am {self.name} of {self.age} years. I am {self.weight} kg. My breed is {self.breed}. " \
               f"I am {self.occupation}."

    def sound(self):
        """
        метод для вывода звука, издающих животными

        :return: Строковое представление объекта.
        """
        print("Woof")

    def movement(self):
        """
        метод для вывода движений, которые могут выполнять жвиотные

        :return: Строковое представление объекта.
        """
        print("I can run and jump")


if __name__ == "__main__":
    # Write your solution here
    Barsik = Cat("Barsik", 5, 7.5, "Oriental")
    Laika = Dog("Laika", 3, 6, "Mixed", "Astronaut")

    print(Barsik)
    Barsik.sound()
    print(Laika)
    Laika.movement()
    Barsik.movement()