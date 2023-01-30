/* 
Forma de decir las diferentes variables
*/
console.log("\n******** Variables ***********\n");
var numero1 = 4;
let numero2 = 6;
const numero3 = 0;
console.log("Numero 1: " + numero1 + " Numero 2: " + numero2);

/*
Cadenas de caracteres
*/
console.log("\n********* Cadenas *********\n");
var frase1 = "Ejemplo de comillas dobles";
let frase2 = 'Ejemplo de comillas simples';
var frase3 = `Ejemplo de comillas ${numero1} invertidas`;

console.log(frase1 + "\n" + frase2 + "\n" + frase3);

/*
Condicionales
*/
console.log("\n*********** Condicionales **********\n");

console.log(numero1 == numero2);
console.log(numero1 < numero2);
console.log(numero1 != numero2);

/*
Operadores logicos, son los que comparan dos veces
*/
console.log("\n********** Operador Logico AND ***********\n");
console.log(true && true);
console.log(true && false);
/*
Recordatorio podemos colocar todos los AND Y OR QUE QUERAMOS, ademas
del uso de parentesis para facilitar cosas
*/
console.log("\n********** Operador Logico OR    ***********\n");
console.log(false || false);
console.log(false || true);

/*
Los arreglos
*/
console.log("\n********** Arreglos *********\n");
let listaDeNumeros = [2, 3, 5, 7, 11, 234];

console.log(listaDeNumeros[5]);

listaDeNumeros.push(16); /* Agrega una nueva variable al arreglo */
listaDeNumeros.push(939);

console.log(listaDeNumeros);
console.log(listaDeNumeros.length);/*Longitud del arreglo */

listaDeNumeros.pop(); /* Quita un numero del final del arreglo */
console.log(listaDeNumeros);
console.log(listaDeNumeros.length);

let listaDePalabras = ["Explorer", "MisionComander", "LaunchX", "Innovaccion"];
console.log(listaDePalabras);
console.log(listaDePalabras.length);

/* Cadena de palabras */
let palabra = "Explorer";
console.log(palabra[2]); /*Indica la letra de esa palabra */
console.log(palabra.length); /*Indica el tamaño */

/* Objetos */
console.log("\n********* Objetos ********\n");

let explorer = {
    nombre: "Josè Miguel Quintana Reyes",
    emain: "jose-san@live.com",
    numReg: 288343,
    mision: "FrontEnd",
    proyectos: ["Abogabot", "Taqueria", "Pasteleria", "Vacunación"],
    proPer: {
        escolar: "Tareas",
        profesional: "Trabajo",
        personal: "Negocio",
        cuantos: 3,
    },
};

console.log(explorer);

console.log(explorer.proPer.escolar);

console.log("Proyectos: " + explorer.proPer.cuantos + " " + explorer.proPer.escolar);

/* Flujo condicional */
let number1 = 10;
let number2 = 6;
console.log("\n********* if / else **********\n");
if (number1 > number2 && number2 > 5) {
    console.log("El número 1 es mayor que número 2");
}
else if ( number1 == number2 || number1 < 3){
    console.log("Los números son iguales");
}
else {
    console.log("El número 2 es mayor que número 1");
}

/* Ciclo condicional */
console.log("\n************ While ************\n");
let numberWhile = 4;
while (numberWhile <= 12) {
    console.log(numberWhile);
    numberWhile = numberWhile + 2;
}

console.log("Aquí ya salió del while " + numberWhile);

/* Ciclo condicional de una iteración mínimo */
console.log("\n************ Do While *******\n");
let numeroDoWhile = 12;
do {
    numeroDoWhile = numeroDoWhile + 2;
    console.log(numeroDoWhile);
} while (numeroDoWhile < 20);
console.log("Aquí sale del Do While " + numeroDoWhile);

/* Ciclo for */
console.log("\n********** For **********\n");
let numeroFor = 0;
for (numeroFor ; numeroFor <= 12; numeroFor = numeroFor + 1) {
    console.log(numeroFor);
}
console.log("Aquì salimos del for" + numeroFor);

/* Swich */
console.log("\n********** Switch **********\n");
switch (prompt("¿Cómo está el clima?")) {
    case "lluvioso":
        console.log("No te vayas a mojar");
        break;
    case "soleado":
        console.log("Ponte bloqueador");
        break;
    case "nublado":
        console.log("Tapate bien");
        break;
    default:
        console.log("No se como está el clima");
        break;
}
console.log("Aqui termina el switch");
