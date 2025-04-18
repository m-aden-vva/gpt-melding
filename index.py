from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Vervang met jouw echte Power Automate URL
POWER_AUTOMATE_URL = "https://prod-244.westeurope.logic.azure.com:443/workflows/2132be8b1bc8451a88cc77bf2ac9ef7d/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=RPHaHrD5kZcSxtioRdhi-QQihPEZx5qqpqo6luoos24"

@app.route("/verzend", methods=["POST"])
def verzend():
    try:
        data = request.json
        response = requests.post(POWER_AUTOMATE_URL, json=data, headers={"Content-Type": "application/json"})
        return jsonify({"status": "success", "power_automate_response": response.text}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
