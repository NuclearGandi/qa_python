from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Филосовский камень')
        assert collector.get_book_genre('Гарри Поттер и Филосовский камень') == ''

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Филосовский камень')
        collector.set_book_genre('Гарри Поттер и Филосовский камень', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер и Филосовский камень') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector =BooksCollector()
        collector.add_new_book('Гарри Поттер и Филосовский камень')
        collector.set_book_genre('Гарри Поттер и Филосовский камень', 'Фантастика')
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фэнтези')
        collector.add_new_book('Темная башня')
        collector.set_book_genre('Темная башня', 'Фантастика')

        books_with_specific_genre = collector.get_books_with_specific_genre('Фантастика')
        assert len(books_with_specific_genre) == 2

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Филосовский камень')
        collector.set_book_genre('Гарри Поттер и Филосовский камень', 'Фантастика')
        collector.add_new_book('Большой куш')
        collector.set_book_genre('Большой куш', 'Комедия')
        collector.add_new_book('Темная башня')
        collector.set_book_genre('Темная башня', 'Фантастика')

        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 1

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Метро 2033')
        assert collector.get_list_of_favorites_books() == ['Метро 2033']

    def test_delete_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Метро 2033')
        collector.delete_book_from_favorites('Метро 2033')
        assert collector.get_list_of_favorites_books() == []