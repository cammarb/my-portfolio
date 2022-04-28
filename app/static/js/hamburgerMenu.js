const primaryNav = document.querySelector(".primary-navigation");
const hamburgerBtn = document.querySelector("#hamburger-button");

hamburgerBtn.addEventListener('click', () => {
    const visibility = primaryNav.getAttribute("data-visible");

    if (visibility === "false") {
        primaryNav.setAttribute("data-visible", true);
    }
    else if (visibility === "true") {
        primaryNav.setAttribute("data-visible", false);
    }
});