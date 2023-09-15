from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post_endpoint', methods=['POST', 'GET'])  # Added 'GET' to the methods list
def post_example():
    if request.method == 'POST':
        data = request.json
        print("Data received:", data)
        app.logger.info(data)
        return jsonify({"message": "Data received", "data": data})
    elif request.method == 'GET':
        return jsonify({"message": "GET request received"})

if __name__ == '__main__':
    app.run(debug=True)
