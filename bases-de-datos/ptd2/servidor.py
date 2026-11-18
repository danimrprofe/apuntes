from flask import Flask, jsonify
import sqlite3  # O usa la biblioteca que prefieras para conectar con tu base de datos

# Crear la aplicación Flask
app = Flask(__name__)

# Función para conectar a la base de datos (ajústala según tu base de datos)
def get_db_connection():
    conn = sqlite3.connect('tu_base_de_datos.db')  # Cambia el nombre de la base de datos
    conn.row_factory = sqlite3.Row  # Esto permite acceder a las columnas por nombre
    return conn

@app.route('/api/hello', methods=['GET'])
def say_hello():
    return "Hello", 200  # Devuelve "Hello" con un código de estado 200 (OK)

# Ruta de la API para obtener los libros
@app.route('/api/libros', methods=['GET'])
def get_libros():
    conn = get_db_connection()
    libros = conn.execute('SELECT * FROM Libros').fetchall()
    conn.close()

    # Convertir los resultados a formato JSON
    libros_list = []
    for libro in libros:
        libros_list.append({
            'ID': libro['ID'],
            'Titulo': libro['Titulo'],
            'ISBN': libro['ISBN'],
            'Editorial': libro['Editorial'],
            'Año_Publicación': libro['Año_Publicación'],
            'Ejemplares_Disponibles': libro['Ejemplares_Disponibles']
        })

    return jsonify(libros_list)

# Ruta de la API para insertar un nuevo libro
@app.route('/api/libros', methods=['POST'])
def insertar_libro():
    # Obtener los datos del libro desde la solicitud JSON
    nuevo_libro = request.get_json()

    # Verificar que los campos necesarios estén presentes
    if not all(key in nuevo_libro for key in ('Titulo', 'ISBN', 'Editorial', 'Año_Publicación', 'Ejemplares_Disponibles')):
        return jsonify({'error': 'Faltan campos requeridos'}), 400  # Retorna un error si falta algún campo

    # Insertar el nuevo libro en la base de datos
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO Libros (Titulo, ISBN, Editorial, Año_Publicación, Ejemplares_Disponibles)
        VALUES (?, ?, ?, ?, ?)
    ''', (nuevo_libro['Titulo'], nuevo_libro['ISBN'], nuevo_libro['Editorial'],
          nuevo_libro['Año_Publicación'], nuevo_libro['Ejemplares_Disponibles']))
    conn.commit()
    conn.close()

    return jsonify({'mensaje': 'Libro insertado con éxito'}), 201  # Retorna un mensaje de éxito

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)