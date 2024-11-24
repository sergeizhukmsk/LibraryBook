import json
import os


class LibraryBook:
    def __init__(self, filename='library.json'):
        self.books = {}  # Инициализация как словарь
        self.filename = filename
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.books = json.load(file)
        else:
            self.books = {}

    def save_books(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, author, title, year):
        book_id = str(len(self.books) + 1)  # Преобразуем в строку, чтобы использовать как ключ
        new_book = {
            'id': book_id,
            'author': author,
            'title': title,
            'year': year,
            'status': 'в наличии'
        }
        self.books[book_id] = new_book  # Добавляем книгу в словарь
        self.save_books()
        print(f'Книга "{title}" добавлена!')

    def remove_book(self, book_id):
        book_id = str(book_id)  # Преобразуем book_id в строку
        if book_id in self.books:
            book = self.books[book_id]
            del self.books[book_id]
            self.save_books()
            print(f'Книга "{book["title"]}" удалена!')
        else:
            print("Книга с указанным id 1111 не найдена.")


    def search_books(self, query):
        results = [book for book in self.books.values() if query.lower() in book['author'].lower() or
                   query.lower() in book['title'].lower() or
                   query == str(book['year'])]
        return results

    def display_books(self):
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books.values():  # Используем .values() для получения значений словаря
            print(
                f'ID: {book["id"]}, Автор: {book["author"]}, Название: {book["title"]}, Год: {book["year"]}, '
                f'Статус: {book["status"]}')

    def change_status(self, book_id, new_status):
        book_id = str(book_id)  # Преобразуем book_id в строку
        if new_status not in ['в наличии', 'выдана']:
            print("Статус должен быть 'в наличии' или 'выдана'.")
            return
        for book in self.books.values():
            if book['id'] == book_id:
                book['status'] = new_status
                self.save_books()
                print(f'Статус книги "{book["title"]}" изменен на "{new_status}".')
                return
        print("Книга с указанным id не найдена.")


# Основная функция формирования меню
def main_menu():

    while True:
        print("\nДоступные команды:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите команду (1-6): ")

        if choice == '1': # Добавить книгу
            author = input("Введите автора книги: ")
            title = input("Введите название книги: ")
            year = input("Введите год издания: ")
            library.add_book(author, title, year)

        elif choice == '2': # Удалить книгу
            book_id = int(input("Введите id книги для удаления: "))
            library.remove_book(book_id)

        elif choice == '3': # Искать книгу
            query = input("Введите автора, название или год для поиска: ")
            results = library.search_books(query)
            if results:
                print("Результаты поиска:")
                for book in results:
                    print(
                        f'ID:{book["id"]},Автор: {book["author"]},Название: {book["title"]},Год: {book["year"]}, '
                        f'Статус: {book["status"]}')
            else:
                print("Книги не найдены.")

        elif choice == '4': # Отобразить все книги
            print("Список всех книг:")
            library.display_books()

        elif choice == '5': # Изменить статус книги
            book_id = int(input("Введите id книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.change_status(book_id, new_status)

        elif choice == '6': # Выход из программы
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    print('__name__ = ', __name__)
    library = LibraryBook()
    library.load_books()
    main_menu()
