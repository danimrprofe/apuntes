from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route('/') # Quan rebem una petició http://127.0.0.1:5000
def benvingut(): # Executarem aquesta funció

    return '''
    Benvingut al meu servidor API! Aquí tens les crides disponibles:
    <br>1. /hola - Mostra "Hola món!"
    <br>2. /adeu - Mostra "Adeu món!"

    '''

@app.route('/hola')
def hola():
    return 'Hola món!'

@app.route('/adeu')
def adeu():
    return 'Adeu món!'

@app.route('/pelicula', methods=['GET'])
def get_movie():
    # Diccionari de pel·lícules amb una pel·lícula per cada número
    peliculas = {
    1: {
        "title": "Origen",
        "genre": "Ciencia ficción",
        "year": 2010
    },
    2: {
        "title": "El padrino",
        "genre": "Crimen, drama",
        "year": 1972
    },
    3: {
        "title": "El caballero oscuro",
        "genre": "Acción, crimen, drama",
        "year": 2008
    }
}
    # Agafa el número de la query string
    number = request.args.get('number', type=int)

    # Comprova si el número és vàlid
    if number in peliculas:
        return jsonify({"movie": peliculas[number]})
    else:
        return jsonify({"error": "Número invàlid. Prova amb 1, 2 o 3."}), 400

if __name__ == '__main__':
    app.run(debug=True)