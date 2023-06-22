// Variable que mantiene el estado visible del carrito
var carritoVisible = false;

// Esperamos que todos los elementos de la pagina se carguen para continuar con el script
if (document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
}else{
    ready();
}

function ready(){
    // Agregamos funcionalidad a los botones eliminar del carrito
    var botonesEliminarItem = document.getElementsByClassName('btn-eliminar');
    for (var i = 0; i < botonesEliminarItem.length; i++){
        var button = botonesEliminarItem[i];
        button.addEventListener('click', eliminarItemCarrito);
    }

    // Agregar funcionalidad al boton sumar
    var botonesSumarCantidad = document.getElementsByClassName('sumar-cantidad');
    for (var i = 0; i < botonesSumarCantidad.length; i++){
        var button = botonesSumarCantidad[i];
        button.addEventListener('click', sumarCantidad);
    }

    // Agregar funcionalidad al boton restar
    var botonesRestarCantidad = document.getElementsByClassName('restar-cantidad');
    for (var i = 0; i < botonesRestarCantidad.length; i++){
        var button = botonesRestarCantidad[i];
        button.addEventListener('click', restarCantidad);
    }

    // Agregar funcionalidad a los botones agregar carrito
    var botonesAgregarCarrito = document.getElementsByClassName('boton-item');
    for (var i = 0; i < botonesAgregarCarrito.length; i++){
        var button = botonesAgregarCarrito[i];
        button.addEventListener('click', agregarCarrito);
    }

    // Agregar funcionalidad al boton realizar pago
    document.getElementsByClassName('btn-pagar')[0].addEventListener('click', pagarClicked)

    // Agregar funcionalidad al icono del carrito
    document.getElementsByClassName('btn-cart')[0].addEventListener('click', aparecerCarrito);
}

// Elimino el item seleccionado del carrito
function eliminarItemCarrito(event){
    var buttonClicked = event.target;
    buttonClicked.parentElement.parentElement.remove(); 

    // Actualizamos el total del carrito, una vez hemos eliminado algun item
    actualizarTotalCarrito();

    // Si no hay elemento, se oculta el carrito
    ocultarCarrito();
}

// Actualizar total carrito
function actualizarTotalCarrito(){
    // Seleccionamos el contenedor carrito
    var carritoContenedor = document.getElementsByClassName('cart')[0];
    var carritoItems = carritoContenedor.getElementsByClassName('cart-item');
    var total = 0;

    // Recorremos cada elemento del carrito para actualizar el total

    for (var i = 0; i < carritoItems.length; i++){
        var item = carritoItems[i];
        var precioElemento = item.getElementsByClassName('carrito-item-precio')[0];
        console.log(precioElemento);

        var precio = parseFloat(precioElemento.innerText.replace('$','').replace('.',''));
        console.log(precio);

        var cantidadItem = item.getElementsByClassName('cart-item-cantidad')[0];
        var cantidad = cantidadItem.value;
        console.log(cantidad);
        
        total = total + (precio * cantidad);
    }
    
    total = Math.round(total * 100) / 100;
    document.getElementsByClassName('carrito-precio-total')[0].innerText = '$' + total.toLocaleString("es") + ',00';
}

function ocultarCarrito(){
    var carritoItems = document.getElementsByClassName('cart-items')[0];
    if (carritoItems.childElementCount == 0){
        var carrito = document.getElementsByClassName('cart')[0];
        carrito.style.marginRight = '-100%';
        carrito.style.opacity = '0';
        carritoVisible = false;

        // Ahora se maximiza el contenedor de los elementos

        var items = document.getElementsByClassName('container-items')[0];
        items.style.width = '100%';
    }
}

function sumarCantidad(event){
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    var cantidadActual = selector.getElementsByClassName('cart-item-cantidad')[0].value;
    console.log(cantidadActual);
    cantidadActual++;
    selector.getElementsByClassName('cart-item-cantidad')[0].value = cantidadActual;

    // Actualizamos el total
    actualizarTotalCarrito();
}

function restarCantidad(event){
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    var cantidadActual = selector.getElementsByClassName('cart-item-cantidad')[0].value;
    console.log(cantidadActual);
    cantidadActual--;

    // Controlamos que no sea menor a 1
    if(cantidadActual >= 1){
        selector.getElementsByClassName('cart-item-cantidad')[0].value = cantidadActual;

        // Actualizamos el total
        actualizarTotalCarrito();
    }
}

function agregarCarrito(event){
    var button = event.target;
    var item = button.parentElement;
    var titulo = item.getElementsByClassName('titulo-item')[0].innerText;
    console.log(titulo);
    var precio = item.getElementsByClassName('precio-item')[0].innerText;
    var imagenSRC = item.getElementsByClassName('img-item')[0].src;

    // Agregamos los productos al carrito
    agregarItemCarrito(titulo, precio, imagenSRC);

    // Hacemos visible el carrito
    // hacerVisibleCarrito();
}

function agregarItemCarrito(titulo, precio, imagenSRC){
    var item = document.createElement('div');
    item.classList.add = 'item';
    var itemsCarrito = document.getElementsByClassName('cart-items')[0];

    // Vamos a controla que el item que esta ingresando no se encuentra ya en el carrito
    var nombreItemsCarrito = itemsCarrito.getElementsByClassName('cart-item-titulo');
    for (var i = 0; i < nombreItemsCarrito.length; i++){
        if (nombreItemsCarrito[i].innerText == titulo){
            alert("El producto ya se encuentra en el carrito");
            return;
        }
    }

    var itemsCarritoContenido = `
    <div class="cart-item">
    
        <img src="${imagenSRC}" alt="" width="80px">
        <div class="cart-item-detalles">

            <span class="cart-item-titulo">${titulo}</span>
            <div class="selector-cantidad">
                        
                <i class="fa-solid fa-minus restar-cantidad"></i>
                <input type="text" value="1" class="cart-item-cantidad" disabled>

                <i class="fa-solid fa-plus sumar-cantidad"></i>

            </div>

            <span class="carrito-item-precio">${precio}</span>

        </div>

        <span class="btn-eliminar">
            <i class="fa-solid fa-trash"></i>
        </span>

    </div>
    `
    item.innerHTML = itemsCarritoContenido;
    itemsCarrito.append(item);

    // Agregamos la funcionalidad a los nuevos botones de los nuevos productos
    item.getElementsByClassName('btn-eliminar')[0].addEventListener('click', eliminarItemCarrito);
    item.getElementsByClassName('sumar-cantidad')[0].addEventListener('click', sumarCantidad);
    item.getElementsByClassName('restar-cantidad')[0].addEventListener('click', restarCantidad);

    actualizarTotalCarrito();
}

function pagarClicked (event){
    // Aqui debemos agregar una condicion de que si el usuario no tiene la sesion activada no puede realizar ninguna compra
    alert("No tienes una sesion activa, Inicie Sesion para poder realizar su compra");

    // Esta funcion es para elimar todo del carrito luego de realizar su compra
    var carritoItems = document.getElementsByClassName('cart-items')[0];
    while(carritoItems.hasChildNodes()){
        carritoItems.removeChild(carritoItems.firstChild);
    }
    actualizarTotalCarrito();

    ocultarCarrito();
}

function hacerVisibleCarrito(){
    carritoVisible = true;
    var carrito = document.getElementsByClassName('cart')[0];
    carrito.style.marginRight = '0';
    carrito.style.opacity = '1';

    var items = document.getElementsByClassName('container-items')[0];
    items.style.width = '60%';
}

function aparecerCarrito (event){
    var visible = event.target;

    if(visible.checked){
        hacerVisibleCarrito();
    } else {
        ocultarCarrito();
    }
}