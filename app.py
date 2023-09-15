from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post_endpoint', methods=['POST'])
def post_example():
    data = request.json
    print("Data received:", data)
    return jsonify({"message": "Data received", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
