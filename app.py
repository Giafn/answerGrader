from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
import routes

# Memuat variabel lingkungan dari file .env
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Register Blueprint dari routes.py
app.register_blueprint(routes.bp)

# Menangani error 404 (Not Found)
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
