// Pobranie elementów
const openMenuPath = document.getElementById("open-menu-path");
const sidebar = document.querySelector(".sidebar");
const openSidebarButton = document.getElementById("open-sidebar-button");
const closeSidebarButton = document.getElementById("close-sidebar-button");
const closeMenuPath = document.getElementById("close-menu-path");

// Otwieranie sidebaru
function showSidebar() {
    sidebar.style.display = 'block';
    openSidebarButton.style.background = '#121314';
    openMenuPath.style.fill = '#fff';
}

// Zamknięcie sidebaru
function closeSidebar() {
    sidebar.style.display = 'none';
}

// Hover na ikonie otwierającej
function openMenuIconHover() {
    openSidebarButton.style.background = "#121314";
    openMenuPath.style.fill = "#fff";
    openSidebarButton.style.transition = "background 200ms";
    openMenuPath.style.transition = "fill 200ms";
}

// Hover-out na ikonie otwierającej
function openMenuIconDisHover() {
    openSidebarButton.style.background = "#fff";
    openMenuPath.style.fill = "#121314";
    openMenuPath.style.transition = "fill 200ms";
    openSidebarButton.style.transition = "background 200ms";
}

// Hover na ikonie zamykającej
function closeMenuIconHover() {
    closeSidebarButton.style.background = "#fff";
    closeMenuPath.style.fill = "#121314";
    closeMenuPath.style.transition = "fill 200ms";
    closeSidebarButton.style.transition = "background 200ms";
}

// Hover-out na ikonie zamykającej
function closeMenuIconDisHover() {
    closeSidebarButton.style.background = "#121314";
    closeMenuPath.style.fill = "#fff";
    closeMenuPath.style.transition = "fill 200ms";
    closeSidebarButton.style.transition = "background 200ms";
}