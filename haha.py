import mysql.connector
import requests

# MySQL 연결
conn = mysql.connector.connect(
    host="localhost",      # MySQL 서버 주소
    user="root",  # MySQL 사용자 이름
    password="1234",  # MySQL 비밀번호
    database="ebookstore"   # 사용할 데이터베이스 이름
)

cursor = conn.cursor()

# API 요청을 보내고 데이터 받기
url = "https://openapi.naver.com/v1/search/book.json"
headers = {
    "X-Naver-Client-Id": "sW_UXKSCFhKIfxOK21j_",  # 여기에 실제 Client ID 입력
    "X-Naver-Client-Secret": "r723lF7d2J"  # 여기에 실제 Client Secret 입력
}
params = {
    "query": "한강",  # 검색할 책 제목
    "display": 50,  # 한 번에 받을 책 개수
    "start": 1  # 검색 시작 위치
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    print("API 요청 성공")
    books = response.json()['items']  # 책 정보 리스트
else:
    print(f"API 요청 실패: {response.status_code}")
    books = []

# 책 데이터를 데이터베이스에 삽입
for book in books:
    book_data = {
        'title': book['title'],
        'author': book['author'],
        'publisher': book['publisher'],
        'isbn': book['isbn'],
        'price': float(book['discount'].replace(",", "")) if book.get('discount') else 0.0,
        'stock_quantity': 10,  # 기본값 설정 (필요시 변경)
        'image_url': book['image'],
        'description': book['description'],
        'pubdate': book['pubdate']
    }

    cursor.execute("""
        INSERT INTO books (title, author, publisher, isbn, price, stock_quantity, image_url, description, pubdate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        book_data['title'],
        book_data['author'],
        book_data['publisher'],
        book_data['isbn'],
        book_data['price'],
        book_data['stock_quantity'],
        book_data['image_url'],
        book_data['description'],
        book_data['pubdate']
    ))

# 변경 사항 커밋
conn.commit()

print(f"{len(books)}개의 책 정보가 성공적으로 삽입되었습니다.")

# 연결 종료
cursor.close()
conn.close()
