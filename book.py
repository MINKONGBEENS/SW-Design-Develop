from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        user='root',        # MySQL 사용자명
        password='1234',    # MySQL 비밀번호
        host='localhost',   # MySQL 서버 주소
        database='ebookstore' # 사용할 데이터베이스
    )
    return conn

@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '')  # 검색어 가져오기

    if query:  # 검색어가 있을 때만 DB에서 검색
        # MySQL 연결
        conn = get_db_connection()
        cursor = conn.cursor()

        # 책 제목을 기준으로 검색 (부분일치)
        cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + query + '%',))  # 튜플로 전달
        books = cursor.fetchall()  # 검색 결과 가져오기

        # MySQL 연결 종료
        cursor.close()
        conn.close()
    else:
        books = []

    # 검색된 책 결과를 템플릿에 전달
    return render_template('search-results.html',  # search-results.html로 렌더링
                           search_term=query, 
                           books=books)

# 기본 경로 추가 (index.html)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
