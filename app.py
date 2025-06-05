from flask import Flask, jsonify

app = Flask(__name__)

with open("blacklist.txt", "r") as file:
    blacklist = set(line.strip() for line in file if line.strip())

@app.route("/<cpf>")
def check_cpf(cpf):
    if cpf in blacklist:
        return jsonify({"status": "BLOCK"})
    else:
        return jsonify({"status": "FREE"})

if __name__ == "__main__":
    app.run(debug=True)
