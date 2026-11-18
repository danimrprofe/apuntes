from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hola():
    return 'Hola món!'

@app.route('/adeu')
def adeu():
    return 'Adeu món!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)