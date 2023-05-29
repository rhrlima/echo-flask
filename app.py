from flask import Flask, request, jsonify

app = Flask(__name__)

methods = ["GET", "POST", "PUT", "DELETE"]

@app.route("/", methods=methods, defaults={"path": ""})
@app.route("/<path:path>", methods=methods)
def echo(path):

    # collect information from the request
    request_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "args": request.args.to_dict(),
        "form": request.form.to_dict(),
        "json": request.get_json(),
    }

    # return the collected information as JSON
    return jsonify(request_info)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
