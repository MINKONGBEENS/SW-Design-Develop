let page = 0; // 로드할 페이지 번호 (Initial page number)
let loading = false; // 콘텐츠가 로드 중인 상태를 나타내는 플래그 (Loading status)

function loadMoreContent() {
    // 만약 로딩 중이라면 함수를 종료하여 중복 로딩을 방지
    if (loading) return;

    loading = true; // 로딩 상태를 true로 설정하여 다른 요청이 오지 않도록 설정
    page += 1; // 페이지 번호를 증가시켜 새로운 콘텐츠를 로드할 준비

    // 임의로 로드할 콘텐츠를 새로 만들기 (예제용)
    const newContent = document.createElement('section'); // 새로운 섹션 엘리먼트 생성
    newContent.classList.add('new-content'); // 새 섹션에 'new-content' 클래스 추가
    newContent.innerHTML = ` 
        <h3>더 많은 콘텐츠 ${page}</h3> 
        <p>페이지 ${page}의 콘텐츠가 추가되었습니다.</p>
    `; // 콘텐츠에 HTML을 추가 (페이지 번호 표시)

    // 특정 컨테이너에 새로운 콘텐츠를 추가
    document.querySelector('.content-container').appendChild(newContent);

    loading = false; // 로딩이 끝났으므로 로딩 상태를 false로 설정
}

// 사용자 슈퍼클래스
class User {
    constructor(userID, name, email, password, authorityLevel) {
      this.userID = userID;
      this.name = name;
      this.email = email;
      this.password = password;
      this.authorityLevel = authorityLevel;
    }
  
    // 계정 삭제
    deleteAccount() {
      console.log(`${this.name}님의 계정이 삭제되었습니다.`);
    }
  
    // 계정 정보 수정
    modifyAccountInfo(newEmail, newPassword) {
      this.email = newEmail;
      this.password = newPassword;
      console.log(`${this.name}님의 계정 정보가 수정되었습니다.`);
    }
  
    // 권한 확인
    verifyAuthority() {
      return this.authorityLevel;
    }
  
    // 도서 조회
    viewBooks() {
      console.log(`${this.name}님이 도서를 조회하고 있습니다.`);
    }
  }
  
  // 일반 사용자 클래스
  class RegularUser extends User {
    constructor(userID, name, email, password, authorityLevel, purchaseHistory = [], wishlist = []) {
      super(userID, name, email, password, authorityLevel);
      this.purchaseHistory = purchaseHistory;
      this.wishlist = wishlist;
    }
  
    // 구매 내역 확인
    checkPurchaseHistory() {
      console.log(`구매 내역: ${this.purchaseHistory.join(', ')}`);
    }
  
    // 위시리스트 추가
    addToWishlist(book) {
      this.wishlist.push(book);
      console.log(`${book}가 ${this.name}님의 위시리스트에 추가되었습니다.`);
    }
  
    // 위시리스트 보기
    viewWishlist() {
      console.log(`${this.name}님의 위시리스트: ${this.wishlist.join(', ')}`);
    }
  }
  
  // 관리자 클래스
  class Admin extends User {
    constructor(userID, name, email, password, authorityLevel) {
      super(userID, name, email, password, authorityLevel);
    }
  
    // 도서 등록 및 수정
    manageBook(book) {
      console.log(`도서 ${book.title}가 등록/수정되었습니다.`);
    }
  
    // 게시판 관리
    managePost(post) {
      console.log(`게시글 ${post.title}이 등록/수정되었습니다.`);
    }
  
    // 도서 정보 수정
    modifyBookInfo(book, newTitle, newAuthor, newPrice) {
      book.title = newTitle;
      book.author = newAuthor;
      book.price = newPrice;
      console.log(`도서 ${newTitle}의 정보가 수정되었습니다.`);
    }
  }
  
  // 전자책 클래스
  class eBook {
    constructor(title, author, publisher, ISBN, price, stock, format) {
      this.title = title;
      this.author = author;
      this.publisher = publisher;
      this.ISBN = ISBN;
      this.price = price;
      this.stock = stock;
      this.format = format;
    }
  
    // 전자책 등록
    addBook() {
      console.log(`${this.title}가 등록되었습니다.`);
    }
  
    // 도서 정보 수정
    modifyBookInfo(newTitle, newAuthor, newPrice) {
      this.title = newTitle;
      this.author = newAuthor;
      this.price = newPrice;
      console.log(`${this.title}의 도서 정보가 수정되었습니다.`);
    }
  
    // 재고 업데이트
    updateStock(newStock) {
      this.stock = newStock;
      console.log(`${this.title}의 재고가 ${newStock}개로 업데이트되었습니다.`);
    }
  
    // DRM 적용
    applyDRM() {
      console.log(`${this.title}에 DRM이 적용되었습니다.`);
    }
  
    // DRM 제거
    removeDRM() {
      console.log(`${this.title}의 DRM이 제거되었습니다.`);
    }
  }
  
  // 도서 판매 클래스
  class BookSales {
    constructor(salesID, userID, bookID, saleDate, paymentStatus) {
      this.salesID = salesID;
      this.userID = userID;
      this.bookID = bookID;
      this.saleDate = saleDate;
      this.paymentStatus = paymentStatus;
    }
  
    // 도서 구매
    purchaseBook() {
      console.log(`도서 ${this.bookID}가 ${this.userID}님에 의해 구매되었습니다.`);
    }
  
    // 결제 처리
    processPayment(amount) {
      this.paymentStatus = '완료';
      console.log(`${amount} 원의 결제가 완료되었습니다.`);
    }
  
    // 영수증 생성
    generateReceipt() {
      console.log(`영수증: ${this.bookID} - ${this.paymentStatus}`);
    }
  }
  
  // 추천 시스템 클래스
  class RecommendationSystem {
    constructor(userBrowsingHistory) {
      this.userBrowsingHistory = userBrowsingHistory;
    }
  
    // 추천 도서 생성
    generateRecommendations() {
      console.log(`추천 도서 목록: ${this.userBrowsingHistory.join(', ')}`);
    }
  }
  
  // 결제 시스템 클래스
  class PaymentSystem {
    constructor(paymentID, userID, paymentAmount, paymentMethod, paymentDate) {
      this.paymentID = paymentID;
      this.userID = userID;
      this.paymentAmount = paymentAmount;
      this.paymentMethod = paymentMethod;
      this.paymentDate = paymentDate;
    }
  
    // 결제 처리
    processPayment() {
      console.log(`${this.paymentAmount} 원의 결제가 ${this.paymentMethod}로 완료되었습니다.`);
    }
  
    // 결제 승인
    approvePayment() {
      console.log(`${this.paymentAmount} 원의 결제가 승인되었습니다.`);
    }
  
    // 결제 거절
    rejectPayment() {
      console.log(`${this.paymentAmount} 원의 결제가 거절되었습니다.`);
    }
  
    // 결제 내역 보기
    viewPaymentHistory() {
      console.log(`결제 내역: ${this.paymentAmount} 원`);
    }
  }
  
  // 위시리스트 클래스
  class Wishlist {
    constructor(userID, bookList = []) {
      this.userID = userID;
      this.bookList = bookList;
    }
  
    // 책을 위시리스트에 추가
    addBookToWishlist(book) {
      this.bookList.push(book);
      console.log(`${book}가 ${this.userID}님의 위시리스트에 추가되었습니다.`);
    }
  
    // 위시리스트에서 책을 제거
    removeBookFromWishlist(book) {
      const index = this.bookList.indexOf(book);
      if (index > -1) {
        this.bookList.splice(index, 1);
        console.log(`${book}가 ${this.userID}님의 위시리스트에서 제거되었습니다.`);
      }
    }
  
    // 위시리스트 보기
    viewWishlist() {
      console.log(`위시리스트: ${this.bookList.join(', ')}`);
    }
  }
  
  // 사용자 활동 기록 클래스
  class UserActivityLog {
    constructor(activityID, userID, activityType, activityDate) {
      this.activityID = activityID;
      this.userID = userID;
      this.activityType = activityType;
      this.activityDate = activityDate;
    }
  
    // 활동 기록 추가
    addActivity() {
      console.log(`${this.activityType} 활동이 기록되었습니다.`);
    }
  
    // 활동 기록 조회
    viewActivity() {
      console.log(`${this.activityType} 활동 기록: ${this.activityDate}`);
    }
  }
  
  // 예시 사용
  const admin = new Admin('admin001', '관리자', 'admin@library.com', 'admin123', 'superadmin');
  const regularUser = new RegularUser('user001', '홍길동', 'user@library.com', 'user123', 'user', [], ['자바스크립트 입문']);
  const ebook = new eBook('자바스크립트 입문', '김지수', '한빛출판사', '123-456-789', 10000, 50, 'pdf');
  const payment = new PaymentSystem('payment001', regularUser.userID, 10000, '카드', new Date());
  
  // 관리자 도서 등록
  admin.manageBook(ebook);
  
  // 일반 사용자 도서 구매
  const bookSale = new BookSales('sale001', regularUser.userID, ebook.title, new Date(), '완료');
  bookSale.purchaseBook();
  bookSale.processPayment(10000);
  bookSale.generateReceipt();
  
  // 추천 시스템 도서 추천
  const recommendation = new RecommendationSystem(['자바스크립트 입문', 'HTML5로 배우는 웹 프로그래밍']);
  recommendation.generateRecommendations();
  
  // 결제 처리
  payment.processPayment();
  
  
