soze전자서점

핵심코드:

============== 고정 헤더 ====================
```
<header>
  <nav class="navbar"> <!-- 네비게이션 바 -->
    <h1 class="logo">SOZE</h1> <!-- 로고 -->
    <ul class="nav-links"> <!-- 네비게이션 링크 -->
      <li><a href="#">웹소설</a></li>
      <li><a href="#">소설</a></li>
      <li><a href="#">오디오북</a></li>
      <li><a href="#">서비스</a></li>
    </ul>
    <div class="auth-links">
      <a href="login.html">LOGIN</a>
      <a href="register.html">SIGN IN</a> -->
    </div> 
  </nav>
</header>
```
============== 설명 ====================

상단에 고정된 헤더로, 로고와 네비게이션 링크(웹소설, 소설, 오디오북 등)를 포함합니다.
사용자 로그인 및 회원가입 버튼이 포함되어 있으며, 사용자의 인증 상태와 페이지 탐색에 중요한 역할을 합니다.

============== 푸터 ====================
```
<div class="footer">
  <span class="footer-title">S O Z E</span>
  <div class="social-icons">
    <div class="social-icon">
      <img src="img/Facebook.png" alt="Facebook" />
    </div>
    <div class="social-icon">
      <img src="img/Twitter.png" alt="Twitter" />
    </div>
    <div class="social-icon">
      <img src="img/Instagram.png" alt="Instagram" />
    </div>
    <div class="social-icon">
      <img src="img/Youtube.png" alt="LinkedIn" />
    </div>
  </div>
  <span class="footer-details">
    TEL. 010-9876-5432 | FAX. 02-3456-9876 | sozeteams@weon.me<br>
    주소: 서울특별시 강남구 역삼동 98-7 6층 543호 | 사업자 등록번호: 14-725-83690 | 대표자: 김망고<br>
    업태: 정보통신업 | 업종: 소프트웨어 개발 및 공급업
  </span>
  <div class="footer-line"></div>
  <div class="footer-links">
    <span class="footer-terms">이용약관</span>
    <span class="footer-privacy">개인정보 처리방침</span>
  </div>
</div>
```
============== 설명 ====================

사이트 하단에 위치한 푸터는 주요 정보(회사 정보, 소셜 미디어 링크 등)를 포함합니다.
이용약관 및 개인정보 처리방침과 같은 법적 문서를 위한 링크도 제공합니다.

============== 추천 도서 섹션 ====================
```
<section class="recommended-books">
  <div class="recommended-header">
    <p class="author-info">한강 작가의 노벨 문학상을 만나보세요</p>
    <h2>NOVEL COLLECTION</h2>
  </div>

  <div class="featured-book">
    <div class="featured-info">
      <div class="book-title">Human Acts</div>
      <div class="book-author">Write By HanKang</div>
      <h3 class="small-title">소년이 온다</h3>
      <p class="author">한강 작가</p>
    </div>
    <div class="image-and-button">
      <img src="img/책 이미지.png" alt="소설 이미지" class="featured-image">
      <a href="#" class="more-button">추천 도서 보러 가기</a>
    </div>
  </div>
  <div class="text-container">
    <p class="left-desc">투명한 보석들같이 허공에 떠서 반짝이기라도 할 것 처럼 너는 눈을 크게 떠본다.</p>
    <p class="right-desc">네모난 밤색 뿔테 안경을 쓴 작은형의 부루퉁한 얼굴이 떠올랐다가...</p>
  </div>
</section>
```
============== 설명 ====================

도서 추천을 위한 섹션으로, 주요 도서와 작가 정보를 강조합니다.
사용자가 관심을 가질 만한 도서 이미지를 포함하며, 관련 정보를 더 자세히 볼 수 있는 버튼을 제공합니다.

============== 검색 ====================
```
<div class="search-container">
    <form action="/search" method="get">
        <div class="search-field">
            <input type="text" name="query" placeholder="검색어를 입력하세요." required>
            <button type="submit" class="search-btn">
                <i class="fas fa-search"></i> <!-- 돋보기 아이콘 -->
            </button>
        </div>
    </form>
</div>
```
============== 설명 ====================

사용자가 입력한 검색어를 서버로 전송하여 도서, 웹소설, 오디오북 등을 검색하는 데 사용됩니다.
돋보기 아이콘과 직관적인 입력 필드를 통해 간편한 검색 경험을 제공합니다.

============== 자유 게시판, 자료실, 이벤트, 공지사항 링크 ====================
```
<li class="dropdown">
    <a href="#">서비스</a>
    <ul class="dropdown-menu">
        <li><a href="community-board.html">자유게시판</a></li>
        <li><a href="datalist-board.html">자료실</a></li>
        <li><a href="event-board.html">이벤트</a></li>
        <li><a href="notice-board.html">공지사항</a></li>
    </ul>
</li>
```
============== 설명 ====================

사용자는 "서비스" 메뉴에서 자유 게시판, 자료실, 이벤트, 공지사항 페이지로 이동할 수 있습니다.
게시판을 통해 사용자 의견을 공유하거나 자료를 업로드하고, 이벤트 참여 및 공지사항을 확인할 수 있습니다.

============== 검색 ====================
```
<section class="today-books">
    <div class="section-header">
        <h2>오늘의 도서</h2>
        <a href="#" class="see-more">더보기</a>
    </div>
    <div class="days-of-week">
        <div class="day-item">
            <img src="static/img/Link_mask-group.png" alt="월요일 도서" class="book-img">
            <p class="book-title">상수리나무 아래</p>
            <p class="book-author">서만, 나무, P, 김수지</p>
            <div class="book-rating">
                <span class="star">★</span>
                <span class="rating-text">4.9 <span>(47,742)</span></span>
            </div>
        </div>
        <!-- 추가 도서 항목 생략 -->
    </div>
</section>
```
============== 설명 ====================

오늘의 도서 섹션은 인기 도서를 추천하여 사용자의 관심을 끌고, 도서 구매 페이지로 연결될 수 있습니다.
평점과 리뷰 수를 표시하여 사용자가 도서를 선택하는 데 도움을 줍니다.


![image](https://github.com/user-attachments/assets/25ef06ac-aa4b-44cb-8f27-357f780a6caf)

로그인 시퀀스 다이어그램 시나리오

1. 사용자 입력

- 사용자가 로그인 화면에서 ID와 비밀번호를 입력합니다.
입력된 데이터는 클라이언트(Front)로 전달됩니다.

2. 로그인 데이터 검증 요청

- Front는 사용자로부터 전달받은 로그인 데이터를 로그인 및 인증 클래스에 전달합니다.

3. 사용자 정보 요청

- 로그인 및 인증 클래스는 데이터베이스(DB)에 사용자 정보 조회를 요청합니다.

4. 사용자 정보 응답

- DB는 요청받은 사용자 정보를 로그인 및 인증 클래스에 응답합니다.

5. 로그인 데이터 검증

- 로그인 및 인증 클래스는 응답받은 사용자 정보를 기반으로 입력된 ID와 비밀번호의 일치 여부를 검증합니다. 검증이 완료되면 검증 결과를 Front로 전달합니다.

6. 로그인 결과 표시

- Front는 검증 결과에 따라 사용자에게 로그인 성공 또는 실패 메시지를 표시합니다.

![image](https://github.com/user-attachments/assets/451d08d9-afd0-4a3f-94cf-ca81a7d36bdf)

사용자 권한 변경 시퀀스 다이어그램 시나리오

1. 사용자 요청

- 사용자가 "사용자 권한 페이지"에 접속하여 권한 변경 요청을 입력합니다.

2. 권한 변경 데이터 전송

- Front는 사용자로부터 입력받은 권한 변경 요청 데이터를 관리자 클래스로 전달합니다.

3. 권한 확인

- 관리자 클래스는 전달받은 데이터를 기반으로 요청 내용을 확인합니다.
확인된 권한 변경 데이터를 적용하기 위해 DB에 업데이트 요청을 보냅니다.

4. 데이터베이스 업데이트

- DB는 요청받은 사용자 권한 데이터를 업데이트합니다.
업데이트 결과를 관리자 클래스로 응답합니다.

5. 결과 응답 및 알림

- 관리자 클래스는 DB로부터 전달받은 업데이트 결과를 Front로 전달합니다.
Front는 사용자에게 권한 변경이 성공적으로 완료되었음을 알리는 메시지를 표시합니다.

![image](https://github.com/user-attachments/assets/00aad1c4-a9ca-425f-9de9-6bd60cbb7073)

이벤트 참여 시퀀스 다이어그램 시나리오

1. 사용자 요청

- 사용자가 이벤트 참여를 요청합니다.
요청 데이터가 Front로 전달됩니다.

2. 이벤트 참여 데이터 전송

- Front는 사용자로부터 받은 이벤트 참여 데이터를 이벤트 클래스로 전달합니다.

3. 이벤트 참여 기록 생성

- 이벤트 클래스는 전달받은 데이터를 사용하여 새로운 이벤트 참여 기록을 생성합니다.
생성된 데이터를 저장하기 위해 DB에 저장 요청을 보냅니다.

4. 이벤트 참여 기록 저장

- DB는 요청받은 이벤트 참여 데이터를 저장합니다.
저장 완료 후 결과를 이벤트 클래스에 응답합니다.

5. 알림 생성

- 이벤트 클래스는 참여 성공 알림을 생성하여 사용자에게 표시할 준비를 합니다.
새로 생성된 알림 데이터를 DB에 저장 요청을 보냅니다.

6. 알림 저장

- DB는 새 알림 데이터를 저장하고 결과를 이벤트 클래스에 응답합니다.

7. 결과 응답 및 메시지 표시

- 이벤트 클래스는 이벤트 참여 성공 메시지와 관련 알림을 Front에 전달합니다.
Front는 사용자에게 성공 메시지와 알림을 표시합니다.

![image](https://github.com/user-attachments/assets/e18356cd-a6f0-48b3-ad9f-097201f8b8ff)

게시판 작성 시퀀스 다이어그램 시나리오
1. 게시판 페이지 접속

- 사용자가 게시판 페이지에 접속합니다.
Front는 게시판 페이지를 사용자에게 로드합니다.

2. 게시글 작성 요청

- 사용자가 게시글 작성 창에 내용을 입력하고 작성 버튼을 클릭합니다.
입력된 데이터는 Front로 전달됩니다.

3. 게시글 데이터 전송

- Front는 사용자가 작성한 게시글 데이터를 게시판 클래스에 전달합니다.

4. 게시글 저장 요청

- 게시판 클래스는 전달받은 데이터를 사용하여 게시글을 저장하기 위해 DB에 저장 요청을 보냅니다.

5. 게시글 저장

- DB는 요청받은 게시글 데이터를 저장합니다.
저장이 완료되면 결과를 게시판 클래스에 응답합니다.

6. 결과 응답

- 게시판 클래스는 DB로부터 받은 저장 결과를 Front에 전달합니다.

7. 결과 표시

- Front는 게시글 작성 결과(성공/실패)를 사용자에게 표시합니다.

![image](https://github.com/user-attachments/assets/f030b969-f699-46e9-b094-600207c256a3)

도서 구매 및 추천 시나리오

1. 도서 선택

- 사용자가 구매할 도서를 선택합니다.
선택된 정보가 도서 판매 클래스로 전달됩니다.

2. 도서 정보 가져오기

- 도서 판매 클래스는 선택된 도서의 세부 정보를 전자책 클래스로 요청합니다.
전자책 클래스는 요청받은 도서 정보를 응답합니다.

3. 결제 요청

- 도서 판매 클래스는 결제 처리를 위해 결제 시스템 클래스에 요청을 보냅니다.
결제 요청에 따라 결제 시스템 클래스는 결제 성공 또는 실패 응답을 반환합니다.

4. 결제 상태 처리

   4-1. 성공 시:

   - 도서 다운로드 요청을 전자책 클래스에 보냅니다.
   전자책 클래스는 도서를 사용자에게 전송합니다.
   도서 판매 클래스는 구매 기록을 사용자 슈퍼 클래스에 추가합니다.

   4-2. 실패 시:

   - 도서 판매 클래스는 결제 실패 메시지를 사용자에게 전달합니다.

5. 구매 기록 확인 및 추천 생성

- 사용자 슈퍼 클래스는 구매 기록을 가져와 추천 시스템 클래스에 전달합니다.
추천 시스템 클래스는 구매 데이터를 기반으로 도서 추천 목록을 생성합니다.
추천된 도서 목록이 사용자에게 반환됩니다.

![image](https://github.com/user-attachments/assets/882aa1bf-86d9-4c0e-812d-eae679d64a18)

검색 기능 시퀀스 다이어그램 시나리오

1. 페이지 접속

- 사용자가 검색 페이지에 접속합니다.
Front는 검색 페이지를 로드하여 사용자에게 표시합니다.

2. 검색어 입력

- 사용자가 검색어를 입력한 후 검색 버튼을 클릭합니다.
입력된 데이터는 Front로 전달됩니다.

3. 검색 요청 전송

- Front는 입력받은 검색어 데이터를 검색 시스템 클래스로 전달합니다.

4. 데이터베이스 조회 요청

- 검색 시스템 클래스는 검색어를 기반으로 관련 데이터를 DB에 요청합니다.

5. 검색 결과 조회

- DB는 검색어와 일치하는 데이터를 조회하여 검색 시스템 클래스에 응답합니다.

6. 검색 결과 반환

- 검색 시스템 클래스는 DB로부터 전달받은 검색 결과를 Front로 전달합니다.

7. 결과 표시

- Front는 사용자에게 검색 결과를 화면에 표시합니다.

![image](https://github.com/user-attachments/assets/e25f55c4-8d6d-420f-9f90-b41ae45315c0)

회원가입 시퀀스 다이어그램 시나리오

1. 회원가입 페이지 접속

- 사용자가 회원가입 페이지에 접속합니다.
Front는 회원가입 페이지를 로드하여 사용자에게 표시합니다.

2. 회원가입 정보 입력

- 사용자가 회원가입 정보를 입력한 후 "Sign Up" 버튼을 클릭합니다.
입력된 데이터는 Front로 전달됩니다.

3. 회원가입 요청 전송

- Front는 입력받은 회원가입 정보를 로그인 및 인증 클래스로 전달합니다.

4. 유효성 검사

- 로그인 및 인증 클래스는 입력받은 회원가입 정보를 검사합니다.

  검사 결과에 따라 두 가지 경우가 있습니다:

    오류 발생 시:
    입력된 정보가 유효하지 않거나 중복된 경우, 오류 메시지를 Front에 반환합니다.
    Front는 사용자에게 오류 메시지를 표시합니다.

    유효성 통과 시:
    로그인 및 인증 클래스는 회원 정보를 저장하기 위해 DB에 요청을 보냅니다.

5. 회원 정보 저장

- DB는 새로운 회원 정보를 저장합니다.
저장 완료 후 결과를 로그인 및 인증 클래스에 응답합니다.

6. 결과 응답 및 표시

- 로그인 및 인증 클래스는 회원가입 성공 메시지를 Front에 전달합니다.
Front는 사용자에게 회원가입 성공 메시지를 표시합니다.
