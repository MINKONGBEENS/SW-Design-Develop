from flask import Flask, render_template

app = Flask(__name__)

# 초기 배너 인덱스
current_index = 0
banners = ['image_2.png', 'image_3.png', 'image_4.png']

# 배너 변경 함수
def change_banner(direction):
    global current_index
    if direction == 'prev':
        current_index = (current_index - 1) % len(banners)  # 이전 배너로 이동
    elif direction == 'next':
        current_index = (current_index + 1) % len(banners)  # 다음 배너로 이동
    return banners[current_index]

@app.route('/')
def index():
    global current_index
    # 현재 배너 이미지 반환
    current_banner = banners[current_index]
    # 이전, 현재, 다음 배너의 이미지 반환
    prev_banner = banners[(current_index - 1) % len(banners)]
    next_banner = banners[(current_index + 1) % len(banners)]
    return render_template('index.html', current_banner=current_banner, prev_banner=prev_banner, next_banner=next_banner)

if __name__ == '__main__':
    app.run(debug=True)
# app.py
from flask import Flask
from config import Config
from dotenv import load_dotenv

# .env 파일을 로드
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

if __name__ == '__main__':
    app.run(debug=True)
