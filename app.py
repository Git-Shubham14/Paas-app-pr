from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello Cloud</h1>
    <p>My web app is deployed using PaaS (Render)</p>
    """

if __name__ == "__main__":
    app.run()