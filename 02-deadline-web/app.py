from datetime import date

from flask import Flask

app = Flask(__name__)

DEADLINES = {
    "Deployment Task 4": "27/09/2026",
    "Project Brief (group)": "04/10/2026",
}


@app.route("/")
def home():
    html = "<h1>SWE40006 deadlines</h1>"
    for item, due in DEADLINES.items():
        days = (date.strptime(due, "%d/%m/%Y") - date.today()).days
        html += f"<p>{item}: {due} ({days} days left)</p>"
    return html


@app.route("/health")
def health():
    return "ok"

app.run(host="0.0.0.0", port=5000)
