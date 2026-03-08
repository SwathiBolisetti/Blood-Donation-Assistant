from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load donor data
with open("donors.json") as f:
    donors = json.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message").lower()

    found = []

    for donor in donors:

        if donor["blood_group"].lower() in user_message:

            if donor["location"].lower() in user_message:

                found.append(donor)

    return jsonify(found)


if __name__ == "__main__":
    app.run(debug=True)