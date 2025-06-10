# 🧪 API de Verificação de CPF em Blacklist

Este projeto é uma API REST desenvolvida em Python utilizando o framework Flask. A API permite verificar se um determinado número de CPF está presente em uma blacklist.
Agora a aplicação permite configurar o arquivo de blacklist por meio da variável de ambiente `BLACKLIST_FILE`, tornando o serviço mais flexível.

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
4. (Opcional) instale as dependências de desenvolvimento para rodar os testes:

   ```bash
   pip install -r requirements-dev.txt
   ```

## 🧪 Como usar

1. **Adicione os CPFs à blacklist:**  
   Insira os CPFs bloqueados, um por linha, no arquivo `blacklist.txt`.

2. **Execute a aplicação:**
   Por padrão o arquivo `blacklist.txt` é utilizado. Caso queira especificar outro caminho, defina a variável de ambiente `BLACKLIST_FILE`.
   ```bash
   BLACKLIST_FILE=/caminho/para/blacklist.txt python app.py
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
   - Se o CPF contiver caracteres inválidos ou número de dígitos incorreto, a API responderá com um erro e código HTTP `400`.

## 🧪 Testes

Instale as dependências de desenvolvimento e execute os testes automatizados com `pytest`:

```bash
pip install -r requirements-dev.txt
pytest
```

## 🛠️ Tecnologias utilizadas

- Python 3.10
- Flask 3.0.2

## 📄 Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Como contribuir

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature ou correção.
3. Envie um pull request.


