function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});

// Cria uma instância do Sortable para a lista ordenável
try {
  const sortableList = new Sortable(document.getElementById('sortable-list'), {
    animation: 150, // Duração da animação em milissegundos
    handle: '.sortable-card', // Elemento usado para arrastar o cartão
    draggable: '.sortable-card', // Elementos que podem ser arrastados
  });
} catch (error) {
  console.log('erro');  
}


// Adicionando Dark Mode
const darkModeToggle = document.getElementById("darkmode-toggle");
const background = document.querySelector("body");
const btn = document.querySelectorAll(".btn");
const form_card = document.querySelector(".form-card");
const textarea = document.querySelectorAll(".autoresize");
const form_card_title = document.querySelector(".form-card-title");
const appbar = document.querySelector(".appbar");
const tag = document.querySelector(".form-card-tag");

// Função para aplicar os estilos do modo noturno
function applyDarkModeStyles() {
  background.classList.add("dark-mode-background");
  form_card.classList.add("dark-mode-background");
  textarea[0].classList.add("dark-mode-background");
  form_card_title.classList.add("dark-mode-background");
  textarea[0].classList.add("dark-mode-text");
  form_card_title.classList.add("dark-mode-text");
  appbar.style.backgroundColor = "#d4aa02";
  btn[0].style.backgroundColor = "#d4aa02";
  try {
    btn[1].style.backgroundColor = "#d4aa02";
    textarea[1].classList.add("dark-mode-background");
    textarea[1].classList.add("dark-mode-text");
  }
  catch (error) {
  }
  try {
    tag.classList.add("dark-mode-background");
    tag.classList.add("dark-mode-text");
  }
  catch (error) {
}}

// Função para remover os estilos do modo noturno
function removeDarkModeStyles() {
  background.classList.remove("dark-mode-background");
  form_card.classList.remove("dark-mode-background");
  textarea[0].classList.remove("dark-mode-background");
  form_card_title.classList.remove("dark-mode-background");
  textarea[0].classList.remove("dark-mode-text");
  form_card_title.classList.remove("dark-mode-text");
  appbar.style.backgroundColor = "#f7d736";
  btn[0].style.backgroundColor = "#f7d736";
  try {
    btn[1].style.backgroundColor = "#f7d736";
    textarea[1].classList.remove("dark-mode-background");
    textarea[1].classList.remove("dark-mode-text");
  }
  catch (error) {
  }
  try{
    tag.classList.remove("dark-mode-background");
    tag.classList.remove("dark-mode-text");
  }
  catch (error) {
}}

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