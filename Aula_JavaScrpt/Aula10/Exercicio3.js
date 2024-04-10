
let numero1 = prompt("Informe o primeiro numero: ")
let sinal = prompt("Informe o sinal: ")

while(sinal != "+" && sinal != "-" && sinal != "/" && sinal != "*") {
    alert("Informe o sinal valido!")
    sinal = prompt("Por favor informe o sinal corretamente: ")
}

let numero2 = prompt("Informe o segundo numero: ")

// Funçao que converte strng para numeros inteiros
numero1 = parseInt(numero1)
numero2 = parseInt(numero2)

let Resultado = 0;

if (sinal == "+"){
    Resultado = numero1 + numero2;
} else if (sinal == "-"){
    Resultado = numero1 - numero2;
} else if (sinal == "/"){
    Resultado = numero1 / numero2;
} else if (sinal == "*"){
    Resultado = numero1 * numero2;
}

alert("Resuldado final é: " + Resultado)