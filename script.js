let page = 0; // 로드할 페이지 번호
let loading = false;

function loadMoreContent() {
    if (loading) return;

    loading = true;
    page += 1;

    // 임의로 로드할 콘텐츠 추가 (예제용)
    const newContent = document.createElement('section');
    newContent.classList.add('collection');
    newContent.innerHTML = `
        <h3>더 많은 컬렉션 ${page}</h3>
        <p>페이지 ${page}의 콘텐츠가 추가되었습니다.</p>
    `;
    document.body.appendChild(newContent);

    loading = false;
}

// 스크롤 이벤트 리스너
document.addEventListener("scroll", function () {
    const header = document.querySelector(".transparent-header");
    if (window.scrollY > 50) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }

    // 스크롤 바닥 감지
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        loadMoreContent();
    }
});
