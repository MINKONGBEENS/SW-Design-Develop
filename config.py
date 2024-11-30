from flask import Flask
from dotenv import load_dotenv
import os

# .env 파일을 로드하여 환경 변수 설정
load_dotenv()

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '1234')
    MYSQL_DB = os.getenv('MYSQL_DB', 'ebookstore')

app = Flask(__name__)
app.config.from_object(Config)

if __name__ == '__main__':
    app.run(debug=True)