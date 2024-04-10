

 function Perso (name , surname , age) {
    this.name = name;
    this.surname = surname;
    this.age = age
 }

 let p1 = new Perso("John" , "Buren" , 25);
 let p2 = new Perso("Beatriz" , "almeida" , 18);


 console.log(p1.name)
 console.log(p2.name) 
 
 console.log("---------------")

function Animal(especie, name) {
    this.especie = especie;
    this.name = name;
}

let a1 = new Animal("Gato: " , "Fiona");
let a2 = new Animal("Cachorro: " , "Topi");

console.log(a1.especie, a1.name)
console.log(a2.especie, a2.name)


