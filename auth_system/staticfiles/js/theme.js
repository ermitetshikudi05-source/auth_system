const root = document.getElementById("themeRoot");

function toggleTheme() {
    const theme = root.getAttribute("data-bs-theme");
    root.setAttribute("data-bs-theme", theme === "dark" ? "light" : "dark");
}
