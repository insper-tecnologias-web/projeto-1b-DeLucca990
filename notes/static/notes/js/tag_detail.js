// Adicionando Dark Mode
const darkModeToggle = document.getElementById("darkmode-toggle");
const background = document.querySelector("body");
const appbar = document.querySelector(".appbar");
const h1 = document.querySelector("h1");
const h2 = document.querySelector("h2");
const content = document.querySelector(".content");
const li = document.querySelectorAll("li");
const strong = document.querySelectorAll("strong");

// Função para aplicar os estilos do modo noturno
function applyDarkModeStyles() {
  background.classList.add("dark-mode-background");
  content.classList.add("dark-mode-background");
  appbar.style.backgroundColor = "#d4aa02";
  h1.classList.add("dark-mode-text");
  h2.classList.add("dark-mode-text");
    for (let i = 0; i < li.length; i++) {
        li[i].classList.add("dark-mode-text");
        strong[i].classList.add("dark-mode-text");
    }
}

// Função para remover os estilos do modo noturno
function removeDarkModeStyles() {
  background.classList.remove("dark-mode-background");
  content.classList.remove("dark-mode-background");
  appbar.style.backgroundColor = "#f7d736";
  h1.classList.remove("dark-mode-text");
  h2.classList.remove("dark-mode-text");
    for (let i = 0; i < li.length; i++) {
        li[i].classList.remove("dark-mode-text");
        strong[i].classList.remove("dark-mode-text");
    }
}

// Verifica se o modo noturno foi ativado anteriormente
const isDarkMode = localStorage.getItem("darkMode") === "true";

// Aplica os estilos de acordo com o status anterior
if (isDarkMode) {
    darkModeToggle.checked = true;
    applyDarkModeStyles();
}

// Listener para alterações no botão de alternância
darkModeToggle.addEventListener("change", () => {
    if (darkModeToggle.checked) {
        applyDarkModeStyles();
        localStorage.setItem("darkMode", "true"); // Armazena no localStorage
    } else {
        removeDarkModeStyles();
        localStorage.setItem("darkMode", "false"); // Armazena no localStorage
    }
});