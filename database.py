import sqlite3

def create_connection(db_file):
    
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    
    sql_create_books_table = """
    CREATE TABLE IF NOT EXISTS books (
        id text PRIMARY KEY,
        title text NOT NULL,
        author text NOT NULL,
        year text NOT NULL,
        isbn text NOT NULL,
        issued_to text,
        history text
    );"""
    cursor = conn.cursor()
    cursor.execute(sql_create_books_table)
    conn.commit()

def insert_book(conn, book):
    
    sql = ''' INSERT INTO books(id, title, author, year, isbn, issued_to, history)
              VALUES(?,?,?,?,?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql, book)
    conn.commit()

def select_all_books(conn):
   
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    return rows

def update_book(conn, book):
    
    sql = ''' UPDATE books
              SET title = ? ,
                  author = ? ,
                  year = ? ,
                  isbn = ? ,
                  issued_to = ? ,
                  history = ?
              WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, book)
    conn.commit()

def delete_book(conn, book_id):
    
    sql = 'DELETE FROM books WHERE id=?'
    cursor = conn.cursor()
    cursor.execute(sql, (book_id,))
    conn.commit()
