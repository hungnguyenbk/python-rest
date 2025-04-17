from flask import Flask
import sys

sys.path.append("/home/hungnv/Documents/project/github/python-rest/rest_structure")

app = Flask(__name__)

# Import controller
from routes.hello_controller import hello_blueprint

# Đăng ký route vào ứng dụng
app.register_blueprint(hello_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
