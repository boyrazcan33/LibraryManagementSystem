class Book:
    
    
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.issued_to = None
        self.history = []

    def issue(self, student):
        
        self.issued_to = student
        self.history.append(student)

    def return_book(self):
        
        self.issued_to = None
