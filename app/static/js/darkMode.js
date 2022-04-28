// Theme Switcher
let darkMode = localStorage.getItem('darkMode');
const switchBtn = document.querySelector("#switch");
const themeSwitcher = document.querySelector("#theme-switcher");


const enableDarkMode = () => {
    document.body.classList.add('dark-mode');
    localStorage.setItem('darkMode', 'enabled');
    switchBtn.classList.add("dark-mode-active");
}

const disableDarkMode = () => {
    document.body.classList.remove('dark-mode');
    localStorage.setItem('darkMode', null);
    switchBtn.classList.remove("dark-mode-active");
}

// If the user already visited and enabled darkMode
if (darkMode === 'enabled') {
    enableDarkMode();
}

themeSwitcher.addEventListener('click', () => {
    darkMode = localStorage.getItem('darkMode');
    if (darkMode !== 'enabled') {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});
