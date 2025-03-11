import re
from library import Library
from book import Book

class LibraryManagementSystem:
    
    
    def __init__(self):
        self.library = Library()

    def is_valid_name(self, name):
        
        return re.match("^[A-Za-z ]*$", name) is not None

    def is_valid_year(self, year):
       
        return re.match("^\d{4}$", year) is not None

    def is_valid_isbn(self, isbn):
        
        return re.match("^\d+$", isbn) is not None

    def add_new_entry(self, title, author, year, isbn):
        
        if not self.is_valid_name(author):
            return "Invalid author name. Must be alphabetic."
        if not self.is_valid_year(year):
            return "Invalid year. Must be a 4-digit number."
        if not self.is_valid_isbn(isbn):
            return "Invalid ISBN. Must be a number."
        
        book = Book(title, author, year, isbn)
        book_id = self.library.add_book(book)
        return f"Book added with ID: {book_id}"

    def view_all_records(self):
        
        return self.library.view_all_books()

    def search_entry(self, search_term):
        
        return self.library.search_books(search_term)

    def update_selected_entry(self, book_id, title=None, author=None, year=None, isbn=None):
        
        if not self.library.books.get(book_id):
            return "Book ID not found."

        if not self.is_valid_name(author):
            return "Invalid author name. Must be alphabetic."
        if not self.is_valid_year(year):
            return "Invalid year. Must be a 4-digit number."
        if not self.is_valid_isbn(isbn):
            return "Invalid ISBN. Must be a number."
        
        if self.library.update_book(book_id, title, author, year, isbn):
            return "Book updated successfully."
        return "Failed to update book."

    def delete_selected_entry(self, book_id):
        
        if self.library.delete_book(book_id):
            return "Book deleted successfully."
        return "Book ID not found."

    def issue_book(self, book_id, student):
        
        if not self.is_valid_name(student):
            return "Invalid student name. Must be alphabetic."
        if self.library.issue_book(book_id, student):
            return "Book issued successfully."
        return "Book cannot be issued."

    def return_book(self, book_id):
        
        if self.library.return_book(book_id):
            return "Book returned successfully."
        return "Book cannot be returned."
