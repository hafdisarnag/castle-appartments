document.addEventListener("DOMContentLoaded", function () {
  const scrollLink = document.querySelector('.scroll-to-openhouses');

  if (scrollLink) {
    scrollLink.addEventListener('click', function (e) {
      // Athuga hvort við séum á heimasíðunni
      if (window.location.pathname === "/" || window.location.pathname === "/home/") {
        e.preventDefault(); // Stöðvum sjálfgefna hegðun
        const section = document.querySelector('#upcoming-open-houses');
        if (section) {
          section.scrollIntoView({ behavior: 'smooth' });
        }
      }
      // Ef við erum ekki á heimasíðunni, leyfum href að virka (fer á /home#upcoming-open-houses)
    });
  }
});
