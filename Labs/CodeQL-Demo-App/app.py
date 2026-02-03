from flask import Flask, request
import yaml
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the vulnerable app!"

@app.route("/yaml", methods=["POST"])
def load_yaml():
    # Vulnerable to YAML deserialization attacks
    data = request.data.decode("utf-8")
    obj = yaml.load(data)  # unsafe load
    return str(obj)

@app.route("/proxy")
def proxy():
    # Vulnerable to SSRF if user controls the URL
    url = request.args.get("url")
    if not url:
        return "Missing url param", 400
    resp = requests.get(url)
    return resp.text

if __name__ == "__main__":
    app.run(debug=True)