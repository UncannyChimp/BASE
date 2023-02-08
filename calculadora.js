const botonsu = document.getElementById("botonsu");
botonsu.addEventListener("click", operacion);

function operacion() {
    let x1 = prompt("Indique el primer numero: ");
    let x2 = prompt("Indique el segundo numero: ");
    console.log(x1);
    console.log(x2);
    let xf = x1 * x2;
    alert(xf);
};