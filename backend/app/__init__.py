from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/')
    def index():
        return jsonify({"message": "VolaPlace API Running"})
    
    @app.route('/api/health')
    def health():
        return jsonify({"status": "healthy"})
    
    return app
