const inputQuantity = document.querySelector('.input-quantity');
const btnIncrement = document.querySelector('#increment');
const btnDecrement = document.querySelector('#decrement');

let valueByDefault = parseInt(inputQuantity.value);

// Funciones para incrementar y descrementar los productos a solicitar

btnIncrement.addEventListener('click', () => {
    valueByDefault += 1;
    inputQuantity.value = valueByDefault;
});

btnDecrement.addEventListener('click', () => {
    if (valueByDefault === 1){
        return
    }

    valueByDefault -= 1;
    inputQuantity.value = valueByDefault;
});

// Toggle
const toggleDescription = document.querySelector('.titulo-descripcion');
const toggleInformation = document.querySelector('.titulo-informacion');
const toggleReviews = document.querySelector('.titulo-reviews');

const contentDescription = document.querySelector('.text-descripcion');
const contentInformation = document.querySelector('.text-informacion');
const contentReviews = document.querySelector('.text-reviews');

toggleDescription.addEventListener('click', () => {
    contentDescription.classList.toggle('hidden')
});

toggleInformation.addEventListener('click', () => {
    contentInformation.classList.toggle('hidden')
});

toggleReviews.addEventListener('click', () => {
    contentReviews.classList.toggle('hidden')
});