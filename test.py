import requests
import json
import hmac
import hashlib
import random
import string
from datetime import datetime

# 발급받은 API Key와 API Secret
API_KEY = 'NCSKHHXCB9BUCQO1'  # API Key
API_SECRET = 'GK3NL3C3WC2B6IUVH8DSFXYKSQSEBMTM'  # API Secret

# SMS 전송 API URL
url = "https://console.coolsms.co.kr/purplebook"

# 현재 시간 가져오기 (UTC 시간, ISO 8601 형식)
date_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

# 랜덤 Salt 생성 (12 ~ 64자)
salt = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(12, 64)))

# Signature 생성
signature = hmac.new(API_SECRET.encode(), f"{date_time}{salt}".encode(), hashlib.sha256).hexdigest()

# 요청 헤더 (Authorization 필드 추가)
headers = {
    "Authorization": f"HMAC-SHA256 apiKey={API_KEY}, date={date_time}, salt={salt}, signature={signature}",
    "Content-Type": "application/json"
}

# 요청 데이터 (JSON)
data = {
    "apiKey": API_KEY,  # apiKey 추가
    "to": "01075024213",  # 수신자 번호
    "from": "01075024213",  # 발신자 번호
    "text": "인증번호는 123456입니다.",  # 메시지 내용
    "type": "sms",  # 메시지 타입
    "date": date_time  # 날짜/시간
}

# POST 요청 보내기
response = requests.post(url, headers=headers, data=json.dumps(data))

# 응답 처리
if response.status_code == 200:
    print("인증번호 전송 성공!")
else:
    print(f"인증번호 전송 실패. Error: {response.status_code}")
    print(response.text)
