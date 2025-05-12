let openhousePage = 2;

document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("openhouses-load-more-btn");
  const container = document.getElementById("openhouses-container");

  if (button) {
    button.addEventListener("click", function () {
        fetch(`/openhouses/load-more-openhouses/?page=${openhousePage}`)
        .then(response => response.text())
        .then(html => {
          if (html.trim() !== "") {
            container.insertAdjacentHTML("beforeend", html);
            openhousePage += 1;
          } else {
            button.style.display = "none";
          }
        });
    });
  }
});

