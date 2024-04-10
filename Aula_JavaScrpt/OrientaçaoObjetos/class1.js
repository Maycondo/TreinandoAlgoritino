class Perso {

    constructor(name , surname , age ){
        this.name = name;
        this.surname = surname;
        this.age = age;
    }


    flando() {
        console.log(`${this.name} ${this.surname} está falando...`)
    }


}


const p1 = new Perso("Maycon" , "douglas" , 20);
const p2 = new Perso("John" , "Buren" , 25);
p1.flando();
p2.flando();


console.log(p1.name)