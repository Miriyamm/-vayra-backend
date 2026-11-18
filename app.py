from dotenv import load_dotenv
load_dotenv()
from flask import Flask, jsonify
from flask_cors import CORS
from core.config import Config
from routes.chat_routes import chat_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# اتصال مسیرها (Routes) به برنامه اصلی
app.register_blueprint(chat_bp)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"status": "error", "message": "آدرس مورد نظر یافت نشد."}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"status": "error", "message": "خطای داخلی سرور."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)