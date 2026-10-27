
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>My Cloud Project</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background: #101827;
            color: white;
            text-align: center;
            padding: 80px 20px;
          }
          .card {
            background: #1e293b;
            padding: 35px;
            border-radius: 15px;
            max-width: 600px;
            margin: auto;
          }
          h1 { color: #60a5fa; }
          p { color: #cbd5e1; }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>My First Cloud Project</h1>
          <p>Built with Python and Flask.</p>
          <p>Deployed on AWS EC2.</p>
          <p>Status: Application is running!</p>
        </div>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
