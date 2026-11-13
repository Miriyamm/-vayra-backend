from flask import Blueprint, request, jsonify
from logic import process_chat_message, get_all_chats, get_chat_messages, create_new_chat

main_bp = Blueprint('main', __name__)

# ۱. ارسال پیام به AI
@main_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"status": "error", "message": "فیلد message الزامی است"}), 400
    
    user_message = data['message']
    chat_id = data.get('chat_id', None) # اگر فرانت نداد، None میشه
    
    new_chat_id, reply = process_chat_message(chat_id, user_message)
    
    return jsonify({"status": "success","chat_id": new_chat_id,"reply": reply}), 200

# ۲. دریافت لیست همه چت‌ها
@main_bp.route('/api/chats', methods=['GET'])
def get_chats():
    chats = get_all_chats()
    return jsonify({"status": "success", "chats": chats}), 200

# ۳. دریافت پیام‌های یک چت خاص
@main_bp.route('/api/chats/<chat_id>', methods=['GET'])
def get_chat(chat_id):
    messages = get_chat_messages(chat_id)
    if messages is not None:
        return jsonify({"status": "success", "messages": messages}), 200
    else:
        return jsonify({"status": "error", "message": "چت پیدا نشد"}), 404

# ۴. ساخت چت جدید
@main_bp.route('/api/chats/new', methods=['POST'])
def new_chat():
    chat_id = create_new_chat()
    return jsonify({"status": "success", "chat_id": chat_id}), 200