

let lista = ["Maycon ", "Luiz", "Maria", "Gabriel"];

// Percorrendo o Array com o for. e mostrando tamanho do array

/*

for(let i = 0; i <lista.length; i++){
    console.log(lista[i])
}

*/

lista.forEach(function(value, index){
    console.log(index)
})