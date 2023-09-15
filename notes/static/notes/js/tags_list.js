// Adicionando Dark Mode
const darkModeToggle = document.getElementById("darkmode-toggle");
const background = document.querySelector("body");
const appbar = document.querySelector(".appbar");
const h1 = document.querySelector("h1");
const a = document.querySelectorAll(".a");
const li = document.querySelectorAll("li");

// Função para aplicar os estilos do modo noturno
function applyDarkModeStyles() {
  background.classList.add("dark-mode-background");
  appbar.style.backgroundColor = "#d4aa02";
  h1.classList.add("dark-mode-text");
  for (let i = 0; i < li.length; i++) {
    a[i].style.backgroundColor = "#d4aa02";
    }
}

// Função para remover os estilos do modo noturno
function removeDarkModeStyles() {
  background.classList.remove("dark-mode-background");
  appbar.style.backgroundColor = "#f7d736";
  h1.classList.remove("dark-mode-text");
  for (let i = 0; i < li.length; i++) {
    a[i].style.backgroundColor = "#f7d736";
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