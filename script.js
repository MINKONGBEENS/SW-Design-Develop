let page = 0; // 로드할 페이지 번호
let loading = false;

function loadMoreContent() {
    if (loading) return;

    loading = true;
    page += 1;

    // 임의로 로드할 콘텐츠 추가 (예제용)
    const newContent = document.createElement('section');
    newContent.classList.add('new-content');
    newContent.innerHTML = `
        <h3>더 많은 콘텐츠 ${page}</h3>
        <p>페이지 ${page}의 콘텐츠가 추가되었습니다.</p>
    `;
    document.querySelector('.content-container').appendChild(newContent); // 새로운 콘텐츠를 특정 컨테이너에 추가

    loading = false;
}