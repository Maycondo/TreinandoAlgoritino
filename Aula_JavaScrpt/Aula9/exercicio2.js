

let AnoNascimento = prompt("Digite o ano de nascimento: ")

while(AnoNascimento >= 2023) {
    alert("Por favor seu de nascimento corretamente.");
    AnoNascimento = prompt("Por favor informe o ano do seu nascimento");

}




let AnoAtual = prompt("Digite o ano atual: ")

let Idade = AnoAtual - AnoNascimento

alert(`Sua idade é ${Idade}`)