import uuid
from book import Book
from database import create_connection, create_table, insert_book, select_all_books, update_book, delete_book

DATABASE = "library.db"

class Library:
   
    
    def __init__(self):
        self.conn = create_connection(DATABASE)
        create_table(self.conn)
        self.books = self.load_books()

    def load_books(self):
        
        books = {}
        rows = select_all_books(self.conn)
        for row in rows:
            book = Book(row[1], row[2], row[3], row[4])
            book.issued_to = row[5]
            book.history = row[6].split(',') if row[6] else []
            books[row[0]] = book
        return books

    def add_book(self, book):
        
        book_id = str(uuid.uuid4())
        self.books[book_id] = book
        book_data = (book_id, book.title, book.author, book.year, book.isbn, book.issued_to, ','.join(book.history))
        insert_book(self.conn, book_data)
        return book_id

    def view_all_books(self):
        
        return self.books

    def search_books(self, search_term):
        
        results = {book_id: book for book_id, book in self.books.items() 
                   if search_term.lower() in book.title.lower() or 
                   search_term.lower() in book.author.lower()}
        return results

    def update_book(self, book_id, title=None, author=None, year=None, isbn=None):
        
        if book_id in self.books:
            book = self.books[book_id]
            if title:
                book.title = title
            if author:
                book.author = author
            if year:
                book.year = year
            if isbn:
                book.isbn = isbn
            book_data = (book.title, book.author, book.year, book.isbn, book.issued_to, ','.join(book.history), book_id)
            update_book(self.conn, book_data)
            return True
        return False

    def delete_book(self, book_id):
        
        if book_id in self.books:
            del self.books[book_id]
            delete_book(self.conn, book_id)
            return True
        return False

    def issue_book(self, book_id, student):
        
        if book_id in self.books and not self.books[book_id].issued_to:
            book = self.books[book_id]
            book.issue(student)
            book_data = (book.title, book.author, book.year, book.isbn, book.issued_to, ','.join(book.history), book_id)
            update_book(self.conn, book_data)
            return True
        return False

    def return_book(self, book_id):
        
        if book_id in self.books and self.books[book_id].issued_to:
            book = self.books[book_id]
            book.return_book()
            book_data = (book.title, book.author, book.year, book.isbn, book.issued_to, ','.join(book.history), book_id)
            update_book(self.conn, book_data)
            return True
        return False
