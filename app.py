from flask import Flask, jsonify
from flask_cors import CORS
from routes import main_bp

app = Flask(__name__)
CORS(app) # این خط اجازه میده فرانت‌اند (React) به بک‌اند وصل بشه

app.register_blueprint(main_bp)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"status": "error", "message": "آدرس مورد نظر یافت نشد."}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"status": "error", "message": "خطای داخلی سرور."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)