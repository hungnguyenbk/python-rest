import json
import requests
from swagger_parser import SwaggerParser

# Đọc file Swagger JSON
def load_swagger_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Tạo API caller từ Swagger
def generate_api_calls(swagger_json, base_url):
    parser = SwaggerParser(swagger_dict=swagger_json)
    print("Error")
    for path, methods in parser.paths.items():
        for method, details in methods.items():
            url = base_url + path.replace("{", "").replace("}", "")  # Format URL
            print(f"API Call: {method.upper()} {url}")

            # Gọi API (chỉ thử nghiệm với GET)
            # if method.lower() == "get":
            #     response = requests.get(url)
            #     print(f"Response ({response.status_code}): {response.text}")

def main():
    # Chạy chương trình với file Swagger
    swagger_file = "/home/hungnv/Documents/project/github/python-rest/read_swagger/swagger.json"
    base_api_url = "https://api.example.com"

    swagger_json = load_swagger_json(swagger_file)
    print(swagger_json["swagger"])
    generate_api_calls(swagger_json, base_api_url)

if __name__ == '__main__':
    main()
