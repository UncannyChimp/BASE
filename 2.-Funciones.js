const cuadrado = function (x) {
    return x * x;
};

let numero = 3;
let numero2 = 2;
let sumaNumerosAlCuadrado = cuadrado(numero) + cuadrado(numero2);
console.log(sumaNumerosAlCuadrado);

/* Funcion que no recibe nada ni regresa nada */

const ruido = function () {
    console.log("kataplum!");
};

ruido();

/* No importa donde este ubicada la funcion, el explorador
la analiza todo al mismo tiempo */

const exponencial = function (base, exponente) {
    let resultado = 1;
    for (let i = 0; i < exponente; i++) {
        resultado *= base;
    }
    return resultado;
};

console.log(exponencial(4, 3));

console.log(sumar(5, 65));

function sumar(x, y) {
    return x+y;
}

/* Funcion flecha */
const restar = (a, b) => {
    return a-b;
}

console.log(restar(40, 8));

function saludar(quien) {
    console.log("Hola " + quien);
    return;
}
saludar("Explorer");
console.log("Bye");


function preguntaDireccion(pregunta) {
    let result = prompt(pregunta);
    if (result,toLowerCase() == "izquierda") return "I";
    if (result.toLowerCase() == "derecha") return "D";
    throw new Error("Direcci{on inv{alida " + result);
}

function mirar() {
    if (preguntaDireccion("A que lado?") == "I") {
        return "Una casa";
    } else {
        return "2 osos hambrientos"
    }
}
