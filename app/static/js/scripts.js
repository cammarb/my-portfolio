/* Theme Switcher */
// the website will allways start in light mode
// so the dark mode is disabled by default
// Dark mode gets created if it doesn’t exist in the LocalStorage 
// if (localStorage.getItem('darkMode') === null) {
//     localStorage.setItem('darkMode', "false");
// }

// checkTheme()

// function checkTheme() {
//     if (localStorage.getItem('darkMode') === false) {
//         var element = document.body;
//         element.classList.remove("dark-mode");
//     }
//     else if (localStorage.getItem('darkMode') === true) {
//         console.log(localStorage.getItem('darkMode'))
//         var element = document.body;
//         element.classList.add("dark-mode");
//     }
// }

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



let theme = localStorage.getItem('data-theme');
const changeThemeToDark = () => {
    document.documentElement.setAttribute("data-theme", "dark") // set theme to dark
    localStorage.setItem("data-theme", "dark") // save theme to local storage
}

const changeThemeToLight = () => {
    document.documentElement.setAttribute("data-theme", "light") // set theme light
    localStorage.setItem("data-theme", 'light') // save theme to local storage
}

// Get the element based on ID
const checkbox = document.getElementById("switch");
// Apply retrived them to the website
checkbox.addEventListener('change', () => {
    let theme = localStorage.getItem('data-theme'); // Retrieve saved them from local storage
    if (theme === 'dark') {
        changeThemeToLight()
    } else {
        changeThemeToDark()
    }
});