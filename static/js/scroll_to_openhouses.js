document.addEventListener("DOMContentLoaded", function () {
  const scrollLink = document.querySelector('.scroll-to-openhouses');

  if (scrollLink) {
    scrollLink.addEventListener('click', function (e) {

      if (window.location.pathname === "/" || window.location.pathname === "/home/") {
        e.preventDefault();
        const section = document.querySelector('#upcoming-open-houses');
        if (section) {
          section.scrollIntoView({ behavior: 'smooth' });
        }
      }

    });
  }
});
