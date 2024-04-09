
function somar(a, b) {
    return `As somas desses dois numeros (${a + b})` ;
}

let somar1 = somar(2, 4)
console.log(somar1);

console.log(`--------------------------------`)

function multiplica(x , y) {
    return `As multiplicaçao desses dois (${x * y})`
    }

    let mult = multiplica (3 , 6 )
    console.log(mult)

console.log(`--------------------------------`)

function perso(name, age){
    return `O usuario ${name} tem ${age} anos.`;
}

let user = perso("Lucas",  20)
console.log(user)

console.log(`--------------------------------`)

function pegarName(parametro){
    if(parametro == 1){
        return  "O parametro foi 1 Luiz";
    } else {
        return "O parametro não foi 1 Maycon"
    }
}

let persoName = pegarName(0)
console.log(persoName)