import os
import requests
import hashlib
import hmac
import time
import random
from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector  # MySQL로 변경

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 세션을 사용하기 위한 비밀 키 설정

# CoolSMS API 정보
API_KEY = 'NCSKHHXCB9BUCQO1'  # API Key
API_SECRET = 'GK3NL3C3WC2B6IUVH8DSFXYKSQSEBMTM'  # API Secret
SENDER_PHONE = '01075024213'  # 발신자 전화번호 (CoolSMS에서 발급받은 번호)

# 인증번호 저장용 딕셔너리 (단기 저장)
verification_codes = {}

# 테스트 모드: True일 경우 실제 문자 발송을 건너뛰고 로그만 출력합니다. False
TEST_MODE = True  # 테스트 중이라면 True로 설정

# 배너 변경 함수
current_index = 0
banners = ['image_2.png', 'image_3.png', 'image_4.png']

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
    current_banner = banners[current_index]
    prev_banner = banners[(current_index - 1) % len(banners)]
    next_banner = banners[(current_index + 1) % len(banners)]
    return render_template('index.html', current_banner=current_banner, prev_banner=prev_banner, next_banner=next_banner)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 인증번호 받기 버튼을 클릭한 경우
        if 'verify_code' in request.form:
            phone_number = request.form['phone']  # 사용자가 입력한 전화번호 받기
            

            # 전화번호 형식 변경: 010-xxxx-xxxx -> +82-10-xxxx-xxxx
            if phone_number.startswith("0"):
                phone_number = "+82" + phone_number[1:]

            # 전화번호가 11자리인지 확인
            if len(phone_number) != 13:  # +82 포함 13자리 (국제번호 + 11자리 전화번호)
                flash("인증번호 전송에 실패했습니다.", "error")  # 전화번호가 11자리 아닌 경우 실패 메시지
                return jsonify({"success": False, "message": "전화번호 형식이 올바르지 않습니다."})  # 실패 응답
            else:
                # 인증번호 생성
                verification_code = str(random.randint(100000, 999999))

                # 인증번호 전송 코드 (CoolSMS API를 사용)
                date_time = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
                salt = str(random.randint(1000000, 9999999))
                data_to_sign = f"api_key={API_KEY}&date={date_time}&salt={salt}"
                signature = hmac.new(API_SECRET.encode(), f"{date_time}{salt}".encode(), hashlib.sha256).hexdigest()

                # 메시지 내용
                message = f"[ 온라인 북스토어 SOZE ]\n\n요청하신 본인인증 인증번호는 {verification_code}입니다."

                # API 요청 URL
                url = 'https://api.coolsms.co.kr/messages/v4/send'

                # 요청 헤더
                headers = {
                    'Authorization': f'HMAC-SHA256 apiKey={API_KEY}, date={date_time}, salt={salt}, signature={signature}',
                    'Content-Type': 'application/json'
                }

                # API 요청 데이터
                data = {
                    "message": {
                        "to": phone_number,  # 수신자 전화번호 (사용자가 입력한 전화번호)
                        "from": SENDER_PHONE,  # 발신자 전화번호 (CoolSMS에서 발급받은 번호)
                        "text": message,  # 메시지 내용
                        "type": "SMS"  # 메시지 타입 (SMS로 설정)
                    }
                }

                # API 요청 보내기
                response = requests.post(url, headers=headers, json=data)

                # 응답 상태 코드 출력 (디버깅용)
                print("Response Status Code:", response.status_code)
                print("Response Text:", response.text)

                try:
                    response_data = response.json()  # 응답을 JSON 형식으로 처리
                    status_code = response_data.get('statusCode')  # statusCode 확인
                    status_message = response_data.get('statusMessage')  # statusMessage 확인

                    # statusCode가 '2000' (정상 접수)인 경우에만 인증번호 전송 성공 처리
                    if status_code == '2000' and '정상 접수' in status_message:
                        verification_codes[phone_number] = verification_code
                        session['phone_number'] = phone_number  # 세션에 전화번호 저장
                        return jsonify({"success": True, "message": "인증번호가 전송되었습니다."})  # 성공 응답
                    else:
                        return jsonify({"success": False, "message": "인증번호 전송에 실패했습니다."})  # 실패 응답
                except ValueError as e:
                    return jsonify({"success": False, "message": f"응답 데이터 형식에 오류가 발생했습니다: {str(e)}"})  # 오류 메시지

        # 인증번호 확인
        elif 'verify_number' in request.form:
            code = request.form['code']  # 사용자가 입력한 인증번호
            phone_number = session.get('phone_number')  # 세션에서 전화번호 가져오기

            if phone_number and verification_codes.get(phone_number) == code:
                # 인증번호가 맞을 경우
                flash("인증이 완료되었습니다.", "success")
                return jsonify({"success": True, "message": "인증이 완료되었습니다."})  # 인증 성공 응답
            else:
                # 인증번호가 틀린 경우
                flash("인증번호가 틀렸습니다. 다시 시도해주세요.", "error")
                return jsonify({"success": False, "message": "인증번호가 틀렸습니다. 다시 시도해주세요."})  # 인증 실패 응답

        # 아이디 유효성 검사 및 회원가입 처리
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # 비밀번호 유효성 검사 (8자 이상)
        if len(password) < 8:
            flash("비밀번호는 8자 이상이어야 합니다.", "error")
            return redirect(url_for('register'))

        # 비밀번호 확인 일치 여부 확인
        if password != confirm_password:
            flash("비밀번호가 일치하지 않습니다.", "error")
            return redirect(url_for('register'))

        # MySQL 연결 설정
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # MySQL 사용자
            password='your_password',  # MySQL 비밀번호
            database='ebookstore'  # 사용하려는 데이터베이스
        )
        cursor = conn.cursor()

        # 아이디 중복 체크
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash("이미 사용 중인 아이디입니다.", "error")
            return redirect(url_for('register'))

        # 비밀번호 해싱
        hashed_password = generate_password_hash(password)

        # 사용자 정보 DB에 삽입
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        conn.close()

        flash("회원가입이 완료되었습니다.", "success")
        return redirect(url_for('login'))  # 회원가입 후 로그인 페이지로 이동

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
from flask import redirect, url_for

# 회원가입 처리 후 리디렉션
@app.route('/register', methods=['POST'])
def register():
    # 회원가입 처리 코드 (이메일, 비밀번호 등)
    
    # 회원가입이 성공하면 로그인 페이지로 리디렉션
    return redirect(url_for('login'))  # 로그인 페이지로 리디렉션