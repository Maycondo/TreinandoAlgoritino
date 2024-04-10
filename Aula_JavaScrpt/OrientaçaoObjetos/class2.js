

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