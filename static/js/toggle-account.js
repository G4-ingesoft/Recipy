let subMenu = document.getElementById('subMenu');
let roundedButton = document.querySelector('.rounded-button');

// Close the submenu when clicking outside of it
document.addEventListener('click', function (event) {
    const isClickInsideSubMenu = subMenu.contains(event.target);
    const isClickInsideRoundedButton = roundedButton.contains(event.target);

    if (!isClickInsideSubMenu && !isClickInsideRoundedButton) {
        subMenu.classList.remove('open-menu');
    }
});

function toggleMenu() {
    subMenu.classList.toggle('open-menu');
}

