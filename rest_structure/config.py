import os
from dotenv import load_dotenv

# Load biến môi trường từ .env
load_dotenv()

port = os.getenv("PORT", "5000")  # Nếu không có PORT, mặc định là 5000
host = os.getenv("HOST", "127.0.0.1")

print(f"Server sẽ chạy trên {host}:{port}")