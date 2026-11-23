import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# اتصال به دیتابیس پیش‌فرض postgres
try:
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='123456',
        host='localhost',
        port='5432'
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    
    # ساخت دیتابیس
    try:
        cursor.execute("CREATE DATABASE vayra_db;")
        print("✅ دیتابیس 'vayra_db' با موفقیت ساخته شد.")
    except psycopg2.errors.DuplicateDatabase:
        print("ℹ️ دیتابیس 'vayra_db' از قبل وجود دارد.")
        
    cursor.close()
    conn.close()

except Exception as e:
    print("❌ خطا در اتصال به دیتابیس:")
    print(e)