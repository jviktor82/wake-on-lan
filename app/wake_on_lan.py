from flask import Flask, request, render_template_string
from wakeonlan import send_magic_packet

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wake on LAN</title>
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }
        .container {
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        img {
            width: 150px;
            margin-bottom: 20px;
        }
        input {
            padding: 8px;
            margin: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="{{ url_for('static', filename='wol.png') }}" alt="Wake on LAN">
        {% if message %}
            <p style="color:green;"><strong>{{ message }}</strong></p>
        {% endif %}
        <form method="POST" action="/">
            <input type="text" id="mac" name="mac" placeholder="AA:BB:CC:DD:EE:FF" required><br>
            <input type="number" id="port" name="port" value="7" required><br>
            <button type="submit">Wake</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def wake_on_lan():
    message = None

    if request.method == "POST":
        mac_address = request.form.get("mac")
        port = int(request.form.get("port"))

        try:
            send_magic_packet(mac_address, port=port)
            message = f"Magic Packet successfully sent to {mac_address} on port {port}!"
        except Exception as e:
            message = f"Error: {e}"

    return render_template_string(html_page, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)