class Book:
    _is_borrowed = False

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def borrow_book(self):
        self._is_borrowed = True

    def return_book(self):
        self._is_borrowed = False

    def get_status(self):
        if self._is_borrowed is True:
            status = f"Книга '{self.title}' автора '{self.author}' кем то взята"
        else:
            status = f"Книга '{self.title}' автора '{self.author}' доступна"

        return status


book1 = Book("Колобок", "Народ")
book1.borrow_book()
book1.return_book()

print(book1.get_status())
