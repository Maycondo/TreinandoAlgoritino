
/*
class Card{
    constructor(name , speed) {
        this.name = name 
        this.speed = speed
    }

    acelerar() {
        if (this.speed >= 100) return;
        this.speed++
    }

    freiar() {
        if (this.velocidade <= 0) return;
        this.speed--
    }

}
*/



class DispositoEletrinico {
    constructor(name) {
        this.name = name
        this.ligado = false;
    }

    ligar() {
        if (this.ligado == true){
            console.log(`O ${this.name} esta ligador`)
            return;
        }

        this.ligado = true;
    }

    desligar() {
        if (!this.ligado){
            console.log(`O ${this.name} ja esta desligador`)
            return;
        }

        this.ligado = false;
    }


}

const d1 = new DispositoEletrinico('Smartphone');
d1.desligar()

console.log(d1)