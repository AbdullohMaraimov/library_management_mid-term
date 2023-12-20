class Book:
    def __init__(self, title, author, genre, price, book_id):
        self._title = title
        self._author = author
        self._genre = genre
        self._price = price
        self._book_id = book_id

    def __str__(self):
        return f"ID: {self._book_id}|Title: {self._title}| Author: {self._author}| Genre: {self._genre}|Price: {self._price}$"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if new_title != "":
            self._title = new_title
        else:
            print("Book title can't be empty")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if new_author != "":
            self._author = new_author
        else:
            print("Author name can't be empty")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if int(new_price) >= 0:
            self._price = int(new_price)
        else:
            print("Price should be non-negative")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, new_genre):
        if new_genre != "":
            self._genre = new_genre
        else:
            print("Genre can't be empty")

    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, new_id):
        self._book_id = new_id
