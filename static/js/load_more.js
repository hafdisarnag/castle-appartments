let currentPage = 1;

document.addEventListener('DOMContentLoaded', function () {
  const loadBtn = document.getElementById('load-more-btn');
  const wrapper = document.querySelector('.properties-container');

  loadBtn.addEventListener('click', function () {
    currentPage += 1;

    fetch(`/property/load-more/?page=${currentPage}`)
      .then(response => response.text())
      .then(html => {
        if (html.trim() === '') {
          loadBtn.style.display = 'none';
        } else {
          wrapper.insertAdjacentHTML('beforeend', html);
        }
      });
  });
});
