import tkinter as tk
from faker import Faker
from library_management_system import LibraryManagementSystem
from gui import LibraryGUI

def populate_sample_data(system, num_books=5):
    
    faker = Faker()
    for _ in range(num_books):
        title = faker.text(max_nb_chars=20)
        author = faker.name()
        year = str(faker.year())
        isbn = str(faker.random_number(digits=10))
        system.add_new_entry(title, author, year, isbn)

if __name__ == "__main__":
    root = tk.Tk()
    system = LibraryManagementSystem()
    populate_sample_data(system)
    gui = LibraryGUI(root)
    root.mainloop()
