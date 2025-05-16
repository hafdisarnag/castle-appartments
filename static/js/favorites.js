document.addEventListener('DOMContentLoaded', function () {
  const forms = document.querySelectorAll('.favorite-form');
  forms.forEach(form => {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const img = form.querySelector('img');
      const formData = new FormData(form);
      const propertyElement = form.closest('.property-item');

      fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
        }
      })
        .then(response => response.json())
        .then(data => {
          if (data.status === 'added') {
            img.src = '/static/images/saved.png';
            showMessage('Property added to favorites', propertyElement);
          } else if (data.status === 'removed') {
            img.src = '/static/images/save.png';
            showMessage('Property removed from favorites', propertyElement);
          }
        })
        .catch(error => console.error('Error:', error));
    });
  });

  function showMessage(text, propertyElement) {
    const messageBox = propertyElement.querySelector('.favorite-message-inside');
    if (!messageBox) return;

    messageBox.textContent = text;
    messageBox.style.display = 'flex';

    setTimeout(() => {
      messageBox.style.display = 'none';
    }, 2000);
  }
});
