from flask import Flask
import platform
import socket

app = Flask(__name__)


@app.route("/")
def home():
    hostname = socket.gethostname()
    system = platform.system()
    release = platform.release()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Python App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #111827;
                color: white;
                text-align: center;
                padding-top: 100px;
            }}

            .container {{
                max-width: 600px;
                margin: auto;
                padding: 40px;
                background: #1f2937;
                border-radius: 15px;
            }}

            h1 {{
                color: #60a5fa;
            }}

            .info {{
                margin-top: 25px;
                line-height: 2;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🐳 Dockerized Python Application</h1>

            <p>Application is running successfully!</p>

            <div class="info">
                <p><strong>Hostname:</strong> {hostname}</p>
                <p><strong>Operating System:</strong> {system}</p>
                <p><strong>Kernel:</strong> {release}</p>
            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
