
// Your JavaScript code here

// Función para mostrar una alerta cuando el usuario hace clic en un botón
function showAlert() {
    alert('Has hecho clic en el botón.');
}

// Función para cambiar el contenido de una tarjeta
function changeCardContent(id, newContent) {
    const card = document.getElementById(id);
    if (card) {
        card.innerHTML = newContent;
    }
}

// Función para añadir un nuevo elemento a una lista
function addToList(listId, newItem) {
    const list = document.getElementById(listId);
    if (list) {
        const listItem = document.createElement('li');
        listItem.textContent = newItem;
        list.appendChild(listItem);
    }
}

// Función para cambiar el tema (por ejemplo, para usuarios con dislexia)
function toggleTheme() {
    const body = document.body;
    if (body.classList.contains('dyslexia-friendly')) {
        body.classList.remove('dyslexia-friendly');
    } else {
        body.classList.add('dyslexia-friendly');
    }
}

// Escucha para el evento de clic en un botón específico
document.addEventListener('DOMContentLoaded', function () {
    const button = document.querySelector('.btn');
    if (button) {
        button.addEventListener('click', showAlert);
    }

    const cards = document.querySelectorAll(".card");
    cards.forEach(card => {
        card.addEventListener("click", function () {
            alert("Has seleccionado una lección");
        });
    });
});

// Actualizar el progreso
function updateProgress(percent) {
    const element = document.getElementById("progress");
    element.style.width = percent + "%";
}

// Cambiar el contenido de la tarjeta
document.getElementById('changeContent').addEventListener('click', function () {
    document.getElementById('cardContent').textContent = 'Nuevo contenido';
});

