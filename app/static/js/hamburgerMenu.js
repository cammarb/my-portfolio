const hamburgerBtn = document.getElementById("hamburger-icon")
let menu = document.getElementById("primary-navigation");

// TODO: Responsive hamburger menu
hamburgerBtn.onclick = () => {
    menu.classList.toggle("show");
};