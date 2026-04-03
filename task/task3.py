class Book:
    def __init__(self, name, author, count=1):
        self.name = name
        self.author = author
        self.count = count

    def __str__(self):
        return f"📖 «{self.name}» | Автор: {self.author} | В наявності: {self.count} шт."


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book):
        for book in self.books:
            if book.name == new_book.name and book.author == new_book.author:
                book.count += 1
                return

        self.books.append(new_book)

    def user_take_book(self, name, author):
        for book in self.books:
            if book.name == name and book.author == author:
                if book.count > 0:
                    book.count -= 1
                    print(f"✅ Ви успішно взяли книгу: «{name}». Залишилось у бібліотеці: {book.count} шт.")
                    return
                else:
                    print(f"❌ Помилка: Усі примірники книги «{name}» (Автор: {author}) наразі видані.")
                    return

        print(f"❌ Помилка: Книги «{name}» (Автор: {author}) не існує в нашій бібліотеці.")

    def show_books(self):
        print("\n" + "=" * 40)
        print("📚 КАТАЛОГ БІБЛІОТЕКИ:")
        print("=" * 40)

        if not self.books:
            print("Бібліотека порожня.")
        else:
            for book in self.books:
                print(book)

        print("=" * 40 + "\n")

if __name__ == "__main__":
    my_library = Library()

    book1 = Book("Кобзар", "Тарас Шевченко", 1)
    book2 = Book("Кобзар", "Тарас Шевченко", 1)
    book3 = Book("1984", "Джордж Орвелл", 2)
    book4 = Book("1984", "Хтось Інший", 1)

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(book4)

    my_library.show_books()

    my_library.user_take_book("Кобзар", "Тарас Шевченко")

    my_library.user_take_book("Кобзар", "Тарас Шевченко")

    my_library.user_take_book("Кобзар", "Тарас Шевченко")

    my_library.user_take_book("Гаррі Поттер", "Джоан Роулінг")

    my_library.show_books()