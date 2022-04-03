/* Theme Switcher */
// the website will allways start in light mode
// so the dark mode is disabled by default
var darkMode = false;

function toggleTheme() {
    darkMode = true;
}

/* Hamburger Menu */

window.onresize = window.onload = function () {
    width = this.innerWidth;

    // Crude way to check that the screen is at least 1024x768
    if (width <= 1024) {
        const parent = document.getElementById('menu-menu');
        const child = document.getElementById('menu-items');
        parent.appendChild(child);
    }
    else {
        const parent = document.getElementById('navbar');
        const child = document.getElementById('menu-items');
        parent.appendChild(child);
    }
}




function toggleMenu() {
    var x = document.getElementById("menu-menu");
    if (x.className === "menu-menu-container") {
        x.className += " responsive";
    } else {
        x.className = "menu-menu-container";
    }
}