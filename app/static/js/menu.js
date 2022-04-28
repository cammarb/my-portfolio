const navigation = document.querySelector(".navigation");
const primaryMenu = document.querySelector(".primary-menu");
const mobileMenu = document.querySelector(".mobile-menu");
const hamburgerBtn = document.querySelector("#hamburger-button");
const themeSwitcher = document.querySelector("#theme-switcher");
const switchBtn = document.querySelector("#switch");

// Hamburger menu
hamburgerBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle("open");
});

window.onresize = window.onload = function () {
    width = this.innerWidth;
    const child = navigation;

    // Check that the screen is at least 1024x768
    if (width <= 1024) {
        const parent = mobileMenu;
        parent.appendChild(child);
    }
    else {
        const parent = primaryMenu;
        parent.appendChild(child);
    }
}

// Theme Switcher
themeSwitcher.addEventListener('click', () => {
    switchBtn.classList.toggle("dark-mode-active");
});