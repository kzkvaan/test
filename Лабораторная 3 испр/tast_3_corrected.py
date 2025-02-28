class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

        if not isinstance(name, str):
            raise TypeError ("Название должно быть строкой !")

        if not isinstance(author, str):
            raise TypeError ("Автор должен быть строкой!")


    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

        if not isinstance(pages, int):
            raise TypeError ("Количество страниц должно быть числом!")

    def pages(self) -> int:
        return self._pages


    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положиельным числом")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self._pages}"
    def __repr__(self):
        return  f'{self.name}, {self.author}, {self._pages}'


class AudioBook(Book):

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

        if not isinstance(duration, float):
            raise TypeError ("Время должно быть числом !")


    def duration(self) -> float:
        return self._duration

    def duration(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError
            raise ValueError
        self._duration = float(value)

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.duration}"
    def __repr__(self):
        return  f'{self.name}, {self.author}, {self.duration()}'


book = PaperBook("Ребекка", "Дафна Дюморье", 1)
print(book)
book.pages = 479
print(book.pages)