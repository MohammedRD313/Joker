from waitress import serve
from app import app  # تأكد من تعديل هذا حسب مسار تطبيقك

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
