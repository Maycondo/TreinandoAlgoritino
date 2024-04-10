class Perso {
    constructor(name , surname , age) {
        this.name = name
        this.surname = surname
        this.age = age 
    }


    falar() {
        return `${this.name} ${this.surname} esta falando que tem ${this.age} anos de idade.`
    }
}

let perso1 = new Perso("John", "Buren", 25)
console.log(perso1.falar())
