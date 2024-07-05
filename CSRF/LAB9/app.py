import flask

app = flask.Flask(__name__)

@app.route("/", methods=["POST"])
def post_payload():
    raw_data = flask.request.data
    print(raw_data.decode("utf-8"))
    # Return a response to avoid errors
    return f"Received raw data: {raw_data.decode('utf-8')}"

app.run("0.0.0.0", "1234")
