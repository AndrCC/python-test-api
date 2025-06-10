import logging
import os
import re
from flask import Flask, jsonify


def load_blacklist(path: str) -> set[str]:
    """Load blacklist entries from the given file."""
    try:
        with open(path, "r") as file:
            return {
                re.sub(r"\D", "", line.strip())
                for line in file
                if line.strip()
            }
    except FileNotFoundError:
        logging.error("Blacklist file '%s' not found.", path)
        return set()


def create_app() -> Flask:
    """Application factory."""
    app = Flask(__name__)
    app.json.ensure_ascii = False

    blacklist_file = os.getenv("BLACKLIST_FILE", "blacklist.txt")
    blacklist = load_blacklist(blacklist_file)
    logging.info("Loaded %d CPFs from %s", len(blacklist), blacklist_file)

    @app.route("/<cpf>")
    def check_cpf(cpf: str):
        if not re.fullmatch(r"[\d\.\-]+", cpf):
            return jsonify({"error": "CPF contém caracteres inválidos."}), 400

        cpf_digits = re.sub(r"\D", "", cpf)

        if len(cpf_digits) != 11:
            return (
                jsonify({"error": "CPF inválido. Deve conter exatamente 11 dígitos."}),
                400,
            )

        status = "BLOCK" if cpf_digits in blacklist else "FREE"
        return jsonify({"status": status})

    return app


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(debug=True)
