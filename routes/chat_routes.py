from flask import Blueprint, request, jsonify
from services.ai_service import process_chat_message, get_all_chats, get_chat_messages, create_new_chat

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"status": "error", "message": "فیلد message الزامی است"}), 400
    
    chat_id = data.get('chat_id', None)
    new_chat_id, reply = process_chat_message(chat_id, data['message'])
    return jsonify({"status": "success", "chat_id": new_chat_id, "reply": reply}), 200

@chat_bp.route('/api/chats', methods=['GET'])
def get_chats():
    return jsonify({"status": "success", "chats": get_all_chats()}), 200

@chat_bp.route('/api/chats/<chat_id>', methods=['GET'])
def get_chat(chat_id):
    messages = get_chat_messages(chat_id)
    if messages is not None:
        return jsonify({"status": "success", "messages": messages}), 200
    return jsonify({"status": "error", "message": "چت پیدا نشد"}), 404

@chat_bp.route('/api/chats/new', methods=['POST'])
def new_chat():
    return jsonify({"status": "success", "chat_id": create_new_chat()}), 200