from flask import Flask, jsonify
import re

app = Flask(__name__)
app.json.ensure_ascii = False

with open("blacklist.txt", "r") as file:
    blacklist = set(
        re.sub(r'\D', '', line.strip()) for line in file if line.strip()
    )

@app.route("/<cpf>")
def check_cpf(cpf):
    if not re.fullmatch(r"[\d\.\-]+", cpf):
        return jsonify({"error": "CPF contém caracteres inválidos."}), 400

    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        return jsonify({"error": "CPF inválido. Deve conter exatamente 11 dígitos."}), 400

    status = "BLOCK" if cpf in blacklist else "FREE"
    return jsonify({"status": status})



if __name__ == "__main__":
    app.run(debug=True)
