import uuid
from datetime import datetime

# دیتابیس موقت در حافظه (چون هنوز دیتابیس اصلی وصل نیست)
db_chats = {}

def create_new_chat():
    chat_id = str(uuid.uuid4())[:8] # ساخت یه آیدی یکتا
    db_chats[chat_id] = {"title": "چت جدید","messages": [],"created_at": datetime.now().isoformat()}
    
    return chat_id

def process_chat_message(chat_id, user_message):
    # اگر chat_id وجود نداشت، یکی بساز
    if not chat_id or chat_id not in db_chats:
        chat_id = create_new_chat()
    
    # اضافه کردن پیام کاربر به تاریخچه
    db_chats[chat_id]["messages"].append({"role": "user", "content": user_message})
    
    # شبیه‌سازی جواب AI (بعدا به OpenAI وصل می‌شه)
    mock_reply = f"من یک هوش مصنوعی هستم. پیام شما این بود: {user_message}"
    
    # اضافه کردن جواب AI به تاریخچه
    db_chats[chat_id]["messages"].append({"role": "assistant", "content": mock_reply})
    
    # اگر عنوان چت "چت جدید" بود، اسمش رو از پیام اول کاربر بذار
    if db_chats[chat_id]["title"] == "چت جدید":
        db_chats[chat_id]["title"] = user_message[:20] + "..."

    return chat_id, mock_reply

def get_all_chats():
    chat_list = []
    for cid, data in db_chats.items():
        chat_list.append({"id": cid, "title": data["title"], "created_at": data["created_at"]})
    return chat_list

def get_chat_messages(chat_id):
    if chat_id in db_chats:
        return db_chats[chat_id]["messages"]
    return None