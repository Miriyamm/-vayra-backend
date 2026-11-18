import uuid
from datetime import datetime

# دیتابیس موقت در حافظه (فعلاً اینجاست تا فاز بعد)
db_chats = {}

def create_new_chat():
    chat_id = str(uuid.uuid4())[:8]
    db_chats[chat_id] = {
        "title": "چت جدید",
        "messages": [],
        "created_at": datetime.now().isoformat()
    }
    return chat_id

def process_chat_message(chat_id, user_message):
    if not chat_id or chat_id not in db_chats:
        chat_id = create_new_chat()
    
    db_chats[chat_id]["messages"].append({"role": "user", "content": user_message})
    
    # شبیه‌سازی AI (فاز بعد به OpenAI وصل میشه)
    mock_reply = f"پاسخ از موتور AI: {user_message}"
    db_chats[chat_id]["messages"].append({"role": "assistant", "content": mock_reply})
    
    if db_chats[chat_id]["title"] == "چت جدید":
        db_chats[chat_id]["title"] = user_message[:20] + "..."

    return chat_id, mock_reply

def get_all_chats():
    return [{"id": cid, "title": data["title"], "created_at": data["created_at"]} for cid, data in db_chats.items()]

def get_chat_messages(chat_id):
    return db_chats.get(chat_id, {}).get("messages", None)