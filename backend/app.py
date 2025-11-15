from flask import Flask, jsonify

app = Flask(__name__)


@app.get('/health')
def health() -> tuple[dict[str, str], int]:
    """Basic health endpoint so the dev server has a target."""
    return jsonify(status='ok'), 200


if __name__ == '__main__':
    app.run(debug=True)
