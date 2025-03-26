import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    message = os.getenv("TEST_MESSAGE")
    return f"<h1>{message}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
