from flask import Flask, jsonify, request
import service

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    request_body = request.get_json()

    result = service.predict(request_body['data'])
    print(result)
    if result == -1:
        return jsonify({"message": "Bad request"}), 400
    else:
        return jsonify({"prediction": result}), 200


if __name__ == "__main__":
    app.run()
