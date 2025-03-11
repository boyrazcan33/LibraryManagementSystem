import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from library_management_system import LibraryManagementSystem

class LibraryGUI:
    

    def __init__(self, root):
        self.system = LibraryManagementSystem()
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#708090")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        main_frame = ttk.Frame(self.root, padding="10", style="MainFrame.TFrame")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(6, weight=1)

        # Styles
        style = ttk.Style()
        style.configure("MainFrame.TFrame", background="#708090")
        style.configure("TLabel", background="#708090", foreground="white", font=("Arial", 12, "bold"))
        style.configure("TEntry", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12, "bold"), background="#FF6F61", foreground="white")
        style.map("TButton", background=[("active", "#FF6F61")])
        style.configure("TMenubutton", font=("Arial", 12, "bold"), background="#40E0D0", foreground="black")
        style.map("TMenubutton", background=[("active", "#40E0D0")])

        # Fonts
        self.label_font = ("Arial", 12, "bold")
        self.entry_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")

        # Input Fields
        ttk.Label(main_frame, text="Title").grid(row=0, column=0, sticky="e")
        self.title_entry = ttk.Entry(main_frame, font=self.entry_font, width=30)
        self.title_entry.grid(row=0, column=1, sticky="w")

        ttk.Label(main_frame, text="Author").grid(row=1, column=0, sticky="e")
        self.author_entry = ttk.Entry(main_frame, font=self.entry_font, width=30)
        self.author_entry.grid(row=1, column=1, sticky="w")

        ttk.Label(main_frame, text="Year").grid(row=2, column=0, sticky="e")
        self.year_entry = ttk.Entry(main_frame, font=self.entry_font, width=30)
        self.year_entry.grid(row=2, column=1, sticky="w")

        ttk.Label(main_frame, text="ISBN").grid(row=3, column=0, sticky="e")
        self.isbn_entry = ttk.Entry(main_frame, font=self.entry_font, width=30)
        self.isbn_entry.grid(row=3, column=1, sticky="w")

        # Dropdown Menu
        action_menu = ttk.Menubutton(main_frame, text="Actions", style="TMenubutton")
        action_menu.grid(row=4, column=0, columnspan=2, pady=10)
        menu = tk.Menu(action_menu, tearoff=0)
        action_menu["menu"] = menu
        menu.add_command(label="Add Book", command=self.add_book)
        menu.add_command(label="Update Book", command=self.update_book)
        menu.add_command(label="Delete Book", command=self.delete_book)
        menu.add_command(label="Issue Book", command=self.issue_book)
        menu.add_command(label="Return Book", command=self.return_book)
        menu.add_separator()
        menu.add_command(label="View All Books", command=self.view_books)
        menu.add_command(label="Search Book", command=self.search_books)
        menu.add_separator()
        menu.add_command(label="Exit", command=self.root.quit)

        # Output Text Box
        self.output_frame = ttk.Frame(main_frame)
        self.output_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")
        self.output_frame.columnconfigure(0, weight=1)
        self.output_frame.rowconfigure(0, weight=1)

        self.output_text = tk.Text(self.output_frame, height=15, wrap="word", font=self.entry_font)
        self.output_text.grid(row=0, column=0, sticky="nsew")

        # Adding Scrollbar to the output text box
        self.scrollbar = ttk.Scrollbar(self.output_frame, orient="vertical", command=self.output_text.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.output_text['yscrollcommand'] = self.scrollbar.set

        # Bind the configure event to adjust font size
        self.root.bind('<Configure>', self.on_resize)

    def on_resize(self, event):
        
        new_font_size = max(12, int(self.root.winfo_height() / 50))
        new_font = ("Arial", new_font_size)
        self.output_text.configure(font=new_font)

    def add_book(self):
        
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        isbn = self.isbn_entry.get()
        if not title or not author or not year or not isbn:
            messagebox.showerror("Add Book", "All fields must be filled.")
            return
        result = self.system.add_new_entry(title, author, year, isbn)
        messagebox.showinfo("Add Book", result)

    def update_book(self):
        
        book_id = simpledialog.askstring("Update Book", "Enter Book ID to update:")
        if book_id:
            title = simpledialog.askstring("Update Book", "Enter new Title:")
            author = simpledialog.askstring("Update Book", "Enter new Author:")
            year = simpledialog.askstring("Update Book", "Enter new Year:")
            isbn = simpledialog.askstring("Update Book", "Enter new ISBN:")
            if not title or not author or not year or not isbn:
                messagebox.showerror("Update Book", "All fields must be filled.")
                return
            result = self.system.update_selected_entry(book_id, title, author, year, isbn)
            messagebox.showinfo("Update Book", result)

    def view_books(self):
        
        books = self.system.view_all_records()
        self.output_text.delete(1.0, tk.END)
        for book_id, book in books.items():
            self.output_text.insert(tk.END, f"{book_id}: {book.title} by {book.author} ({book.year}) [ISBN: {book.isbn}]\n")

    def search_books(self):
        
        search_term = simpledialog.askstring("Search Book", "Enter title or author to search:")
        if search_term:
            books = self.system.search_entry(search_term)
            self.output_text.delete(1.0, tk.END)
            for book_id, book in books.items():
                self.output_text.insert(tk.END, f"{book_id}: {book.title} by {book.author} ({book.year}) [ISBN: {book.isbn}]\n")

    def delete_book(self):
        
        book_id = simpledialog.askstring("Delete Book", "Enter Book ID to delete:")
        if book_id:
            result = self.system.delete_selected_entry(book_id)
            messagebox.showinfo("Delete Book", result)

    def issue_book(self):
        
        book_id = simpledialog.askstring("Issue Book", "Enter Book ID to issue:")
        if book_id:
            student = simpledialog.askstring("Issue Book", "Enter student name:")
            if student:
                result = self.system.issue_book(book_id, student)
                messagebox.showinfo("Issue Book", result)

    def return_book(self):
        
        book_id = simpledialog.askstring("Return Book", "Enter Book ID to return:")
        if book_id:
            result = self.system.return_book(book_id)
            messagebox.showinfo("Return Book", result)

if __name__ == "__main__":
    root = tk.Tk()
    gui = LibraryGUI(root)
    root.mainloop()
