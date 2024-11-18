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
