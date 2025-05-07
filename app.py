from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Aplicación desplegada exitosamente!'

@app.route('/status')
def status():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run()