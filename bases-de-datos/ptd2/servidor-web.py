from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_books():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Libro, Titulo, Editorial, ISBN, Anio_Publicacion FROM Libros")
    books = cursor.fetchall()
    conn.close()
    return books

@app.route('/')
def index():
    books = get_books()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)