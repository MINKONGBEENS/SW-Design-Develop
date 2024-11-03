
// 무한 스크롤 설정
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

window.addEventListener('scroll', () => {
  // 스크롤이 페이지 끝에 도달할 경우 콘텐츠 추가
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
    loadMoreContent();
  }
});