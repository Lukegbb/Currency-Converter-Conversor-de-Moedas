# Currency Converter / Conversor de Moedas

This project is a web-based currency converter that allows users to convert between different currencies in real-time using the latest exchange rates. The application is built using Flask for the backend and Bootstrap for the frontend, offering a clean, responsive, and easy-to-use interface.

Este projeto é um conversor de moedas baseado na web que permite aos usuários converter entre diferentes moedas em tempo real, usando as últimas taxas de câmbio. A aplicação foi desenvolvida usando Flask para o backend e Bootstrap para o frontend, oferecendo uma interface limpa, responsiva e fácil de usar.

## Table of Contents / Índice

- [Features / Funcionalidades](#features--funcionalidades)
- [Technologies Used / Tecnologias Utilizadas](#technologies-used--tecnologias-utilizadas)
- [Project Structure / Estrutura do Projeto](#project-structure--estrutura-do-projeto)
- [Installation / Instalação](#installation--instalação)
- [Usage / Uso](#usage--uso)
- [API Source / Fonte da API](#api-source--fonte-da-api)
- [Future Improvements / Melhorias Futuras](#future-improvements--melhorias-futuras)
- [License / Licença](#license--licença)

## Features / Funcionalidades

- **Convert between various currencies** (USD, EUR, GBP, BRL, etc.).
- **Real-time exchange rates** fetched from an external API.
- **Responsive design** with a mobile-friendly layout.
- **Conversion history** that displays recent conversions.
- **Error handling** for invalid inputs and failed API requests.
- **User-friendly interface** designed using Bootstrap.

- **Converter entre várias moedas** (USD, EUR, GBP, BRL, etc.).
- **Taxas de câmbio em tempo real** obtidas de uma API externa.
- **Design responsivo**, compatível com dispositivos móveis.
- **Histórico de conversões** que exibe as conversões recentes.
- **Tratamento de erros** para entradas inválidas e falhas na API.
- **Interface amigável**, projetada usando Bootstrap.

## Technologies Used / Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: Bootstrap, HTML, CSS, JavaScript
- **API**: ExchangeRate API for fetching real-time exchange rates
- **Other Libraries**: requests (for API requests), cachetools (for caching)

- **Backend**: Flask (Python)
- **Frontend**: Bootstrap, HTML, CSS, JavaScript
- **API**: ExchangeRate API para obter taxas de câmbio em tempo real
- **Outras Bibliotecas**: requests (para requisições à API), cachetools (para cache)

  ## Installation / Instalação

To set up the project on your local machine, follow these steps:

Para configurar o projeto na sua máquina local, siga os passos abaixo:

1. **Clone the repository / Clone o repositório:**
    ```bash
    git clone https://github.com/yourusername/currency-converter.git
    cd currency-converter
    ```

2. **Create a virtual environment and activate it / Crie um ambiente virtual e ative-o:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate` / No Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies / Instale as dependências necessárias:**
    ```bash
    pip install -
Flask

requests

cachetools

Bootstrap (CDN)
    ```

4. **Run the application / Execute a aplicação:**
    ```bash
    python app.py
    ```

5. **Open your browser and go to** `http://127.0.0.1:5000/` **to access the application / Abra o navegador e vá para** `http://127.0.0.1:5000/` **para acessar a aplicação.**

## Usage / Uso

### Main Interface / Interface Principal

1. **Select the base currency**: Choose the currency you want to convert from by selecting it from the first dropdown menu. (e.g., USD for U.S. dollars) / Escolha a moeda base que você deseja converter no primeiro menu suspenso. (por exemplo, USD para dólares americanos)

2. **Select the target currency**: Choose the currency you want to convert to from the second dropdown menu. (e.g., EUR for euros) / Escolha a moeda de destino no segundo menu suspenso. (por exemplo, EUR para euros).

3. **Enter the amount**: Input the amount of money you want to convert in the input field. (e.g., 100) / Insira o valor que deseja converter no campo de entrada. (por exemplo, 100).

4. **Click on Convert**: Click the "Convert" button to calculate the conversion based on the latest exchange rate / Clique no botão "Converter" para calcular a conversão com base na última taxa de câmbio.

5. **View the results**: The result of the conversion will be displayed under the input field with both the original amount and the converted value / O resultado da conversão será exibido abaixo do campo de entrada, com o valor original e o valor convertido.

6. **Check conversion history**: Previous conversions will be displayed below the result area for quick reference / As conversões anteriores serão exibidas abaixo da área de resultados para fácil referência.

### Error Handling / Tratamento de Erros

- If the user inputs an invalid value (e.g., letters instead of numbers), an error message will be displayed, prompting the user to enter a valid number / Se o usuário inserir um valor inválido (como letras em vez de números), uma mensagem de erro será exibida, pedindo que o usuário insira um número válido.

- If there is an issue with the API request (e.g., no internet connection), an error message will be displayed informing the user that the conversion could not be processed / Se houver um problema com a solicitação à API (como falta de conexão com a internet), uma mensagem de erro será exibida, informando que a conversão não pôde ser processada.

### Detailed Usage Guide / Guia Detalhado de Uso

#### Conversion Process / Processo de Conversão

1. **Selecting Currencies**: The application provides a dropdown menu for selecting both the base and target currencies. Users can choose from various major currencies (e.g., USD, EUR, GBP, BRL) to make conversions. Ensure that both currencies are selected correctly for accurate results.

   - **Selecionando Moedas**: A aplicação oferece um menu suspenso para selecionar tanto a moeda base quanto a moeda de destino. Os usuários podem escolher entre várias moedas principais (como USD, EUR, GBP, BRL) para realizar conversões. Certifique-se de que ambas as moedas estejam selecionadas corretamente para resultados precisos.

2. **Input Amount**: Once the currencies are selected, the user must enter the amount to convert. Only numeric inputs are accepted, and decimal values are supported. If an invalid input is provided (e.g., letters or symbols), the application will prompt the user to enter a valid amount.

   - **Inserir Quantidade**: Uma vez que as moedas estão selecionadas, o usuário deve inserir o valor a ser convertido. Apenas entradas numéricas são aceitas, e valores decimais são suportados. Se uma entrada inválida for fornecida (como letras ou símbolos), a aplicação pedirá ao usuário que insira um valor válido.

3. **Conversion Results**: After clicking "Convert", the application will fetch the latest exchange rate from the ExchangeRate API and display the converted value. The result is shown immediately under the input field, including both the original amount and the converted result.

   - **Resultados da Conversão**: Após clicar em "Converter", a aplicação buscará a última taxa de câmbio da API ExchangeRate e exibirá o valor convertido. O resultado é mostrado imediatamente abaixo do campo de entrada, incluindo o valor original e o resultado da conversão.

4. **History**: The conversion history is updated each time a conversion is performed, displaying recent transactions for the user to review or refer back to.

   - **Histórico**: O histórico de conversão é atualizado cada vez que uma conversão é realizada, exibindo as transações recentes para que o usuário possa revisar ou consultar.

## API Source / Fonte da API

The exchange rates are fetched from the ExchangeRate API, which provides real-time currency conversion rates for various currencies.

As taxas de câmbio são obtidas da ExchangeRate API, que fornece taxas de conversão de moedas em tempo real para várias moedas.


## Project Structure / Estrutura do Projeto

```bash
currency-converter/
│
├── app.py               # Main application file
├── templates/
│   └── index.html       # HTML template for the frontend
├── static/
│   ├── css/
│   │   └── styles.css   # Custom CSS styles
│   └── js/
│       └── script.js    # JavaScript logic for frontend interactions
├── cache/
│   └── cache.json       # Caching of exchange rates (optional)
├── requirements.txt     # List of Python dependencies
├── README.md            # Project documentation
└── LICENSE              # License information
