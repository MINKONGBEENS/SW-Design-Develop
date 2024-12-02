from flask import Flask, render_template, redirect, url_for

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
def home():
    global current_index
    banners = ['image_2.png', 'image_3.png', 'image_4.png']

    current_banner = banners[current_index]
    prev_banner = banners[(current_index - 1) % len(banners)]
    next_banner = banners[(current_index + 1) % len(banners)]

    return render_template('index.html', current_banner=current_banner, prev_banner=prev_banner, next_banner=next_banner)

# 로그인 페이지 라우트
@app.route('/login')
def login():
    return render_template('login.html')

# 회원가입 페이지 라우트
@app.route('/register')
def register():
    return render_template('register.html')

# 자유게시판 페이지 라우트
@app.route('/community-board')
def community_board():
    return render_template('community-board.html')

# 자료실 페이지 라우트
@app.route('/datalist-board')
def datalist_board():
    return render_template('datalist-board.html')

# 이벤트 페이지 라우트
@app.route('/event-board')
def event_board():
    return render_template('event-board.html')

# 공지사항 페이지 라우트
@app.route('/notice-board')
def notice_board():
    return render_template('notice-board.html')

if __name__ == '__main__':
    app.run(debug=True)
