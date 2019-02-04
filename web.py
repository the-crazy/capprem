from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os

app = Flask(__name__)


@app.route('/api/v1/resultados', methods=['GET'])
def resultados():
    html_doc = urlopen(
        "http://www.capitaldepremios.com.br/resultados-atualizado/").read()
    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    for Results in soup.find_all("div", class_="results"):
        grupo = Results.find("div", class_="grupo").find(
            "lu", class_="numeros")

        data.append({'numeros': Results.text.strip()})
        return jsonify({'Resultado': data})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='127.0.0.1', port=port)
