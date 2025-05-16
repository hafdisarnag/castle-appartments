document.addEventListener("DOMContentLoaded", function () {

    const editBtn = document.getElementById("toggle-edit-btn");
    const editForm = document.getElementById("edit-profile-form");

    if (editBtn && editForm) {
        editBtn.addEventListener("click", function () {
            editForm.classList.toggle("d-none");
        });
    }


    const toggleBtn = document.getElementById('toggle-saved-btn');
    const extraCards = document.querySelectorAll('.extra-property');
    let showingAll = false;

    if (toggleBtn && extraCards.length) {
        toggleBtn.addEventListener('click', function () {
            extraCards.forEach(card => card.classList.toggle('d-none'));
            toggleBtn.textContent = showingAll
                ? 'View all Saved properties'
                : 'Hide extra Saved properties';
            showingAll = !showingAll;
        });
    }
});
