from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Base URL of third-party API
BASE_URL = "https://jsonplaceholder.typicode.com"


# Route for posts
@app.route('/posts', methods=['GET'])
def get_posts():
    try:
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


# Route for comments
@app.route('/comments', methods=['GET'])
def get_comments():
    try:
        response = requests.get(f"{BASE_URL}/comments")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


# Route for albums
@app.route('/albums', methods=['GET'])
def get_albums():
    try:
        response = requests.get(f"{BASE_URL}/albums")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Flask API is running",
        "available_routes": ["/posts", "/comments", "/albums"]
    })


if __name__ == '__main__':
    app.run(debug=True)