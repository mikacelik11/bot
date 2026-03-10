from flask import Flask, request, jsonify, render_template
from bot import get_response

app = Flask(__name__)


# -------------------------------------------------------
# ROUTE
# -------------------------------------------------------

@app.route("/")
def index():
    """Serves the main chat page."""
    # TODO: Make sure templates/index.html exists
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """
    Receives a JSON body like: { "message": "hello" }
    Returns a JSON response like: { "reply": "Hey there!" }
    """
    data = request.get_json()

    # TODO: Add input validation (what if message is empty?)
    user_message = data.get("message", "")

    bot_reply = get_response(user_message)

    return jsonify({"reply": bot_reply})


# -------------------------------------------------------
# RUN
# -------------------------------------------------------
if __name__ == "__main__":
    # debug=True auto-reloads when you save changes
    app.run(debug=True)