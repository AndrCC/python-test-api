# 🧪 API de Verificação de CPF em Blacklist

Este projeto é uma API REST desenvolvida em Python utilizando o framework Flask. A API permite verificar se um determinado número de CPF está presente em uma blacklist.

## 🚀 Pré-requisitos

- Python 3.10+
- Git

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/python-test-api.git
   cd python-test-api
   ```

2. Crie e ative o ambiente virtual:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # No Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Como usar

1. **Adicione os CPFs à blacklist:**  
   Insira os CPFs bloqueados, um por linha, no arquivo `blacklist.txt`.

2. **Execute a aplicação:**  
   ```bash
   python app.py
   ```

3. **Faça uma requisição:**  
   Acesse a API pelo navegador ou por ferramentas como `curl` ou Postman:

   ```
   http://127.0.0.1:5000/<cpf>
   ```
   Exemplo:
   ```
   http://127.0.0.1:5000/00000000000
   ```

4. **Resposta da API:**  
   - Se o CPF não estiver na blacklist:
     ```json
     {
       "status": "FREE"
     }
     ```
   - Se o CPF estiver na blacklist:
     ```json
     {
       "status": "BLOCK"
     }
     ```

## 🧪 Testes

Você pode testar manualmente utilizando o comando abaixo:

```bash
curl http://127.0.0.1:5000/00000000000
```

A resposta será um JSON indicando o status do CPF consultado.

## 🛠️ Tecnologias utilizadas

- Python 3.10
- Flask 3.0.2

## 📄 Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Como contribuir

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature ou correção.
3. Envie um pull request.


