from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Sbruzzi's APPs"

if __name__ == '__main__':
    app.run()