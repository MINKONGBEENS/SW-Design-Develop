from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    # MySQL 연결 정보 (비밀번호: 1234)
    conn = mysql.connector.connect(
        user='root',          # MySQL 사용자명
        password='1234',      # MySQL 비밀번호
        host='localhost',     # MySQL 서버 주소
        database='ebookstore' # 사용할 데이터베이스
    )
    return conn

@app.route('/search', methods=['GET'])
def search_books():
    # 사용자가 검색한 검색어를 받아옴
    query = request.args.get('query', '')  # 검색어 가져오기

    # MySQL 연결
    conn = get_db_connection()
    cursor = conn.cursor()

    # 책 제목을 기준으로 검색 (부분일치)
    cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + query + '%'))
    books = cursor.fetchall()  # 검색 결과 가져오기

    # MySQL 연결 종료
    cursor.close()
    conn.close()

    # 검색된 책 결과를 템플릿에 전달
    return render_template('search_results.html', 
                           search_term=query, 
                           books=books)

if __name__ == '__main__':
    app.run(debug=True)