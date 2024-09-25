from flask import Flask, render_template, request, jsonify
import requests
from cachetools import TTLCache

app = Flask(__name__)

# Cache de taxas de câmbio (TTL de 1 hora)
exchange_rate_cache = TTLCache(maxsize=100, ttl=3600)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.json
        base_currency = data['base'].upper()
        target_currency = data['target'].upper()
        amount = float(data['amount'])

        # Validação do valor inserido
        if amount <= 0:
            return jsonify({'error': 'Valor inválido. O valor deve ser maior que 0.'}), 400

        # Verifica se já temos as taxas em cache
        if base_currency in exchange_rate_cache:
            exchange_rates = exchange_rate_cache[base_currency]
        else:
            api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
            response = requests.get(api_url)
            if response.status_code != 200:
                return jsonify({'error': 'Erro ao obter taxas de câmbio.'}), 500
            exchange_rates = response.json()['rates']
            exchange_rate_cache[base_currency] = exchange_rates

        # Verifica se a moeda de destino está nas taxas de câmbio
        if target_currency in exchange_rates:
            conversion_rate = exchange_rates[target_currency]
            converted_amount = amount * conversion_rate
            return jsonify({'converted_amount': round(converted_amount, 2)})
        else:
            return jsonify({'error': 'Moeda de destino não suportada.'}), 400

    except ValueError:
        return jsonify({'error': 'O valor deve ser numérico.'}), 400
    except Exception as e:
        return jsonify({'error': 'Erro interno no servidor.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
